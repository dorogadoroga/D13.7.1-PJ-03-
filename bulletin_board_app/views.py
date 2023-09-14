from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

from .models import *
from .forms import PostForm, CommentForm
from .filters import CommentFilter


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        post = Post.objects.get(id=self.kwargs['pk'])
        comments = []
        for comment in post.comments.all():
            if comment.is_accepted:
                comments.append(comment)
        context['accepted_comments'] = comments
        return context


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostsByCategoryView(ListView):
    template_name = 'posts_by_category.html'
    model = Post
    context_object_name = 'posts_by_category'
    ordering = ['-id']
    paginate_by = 30

    def get_queryset(self, *args, **kwargs):
        category = self.request.path.split('/')[-1]
        queryset = Post.objects.filter(category__slug=category)
        return queryset


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add_post.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        url = f'/{self.request.user.id}/account'
        print(url)
        form = self.form_class(request.POST, request.FILES)
        form.instance.author = self.request.user
        if form.is_valid():
            form.save()
        return redirect(url)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'edit_post.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_post.html'
    success_url = '/index'

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(author=user)
        return queryset

class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'personal_comments.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        queryset = Comment.objects.filter(post__author=user).order_by('-id')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['filter'] = CommentFilter(self.request.GET, user=self.request.user, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        url = self.request.path
        if request.method == 'POST':
            comment = Comment.objects.get(id=request.POST['comment_id'])
            if request.POST['action'] == 'accept':
                comment.is_accepted = True
                comment.save()
            elif request.POST['action'] == 'delete':
                comment.delete()
        return redirect(url)



class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add_comment.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.author = self.request.user
        post = Post.objects.get(id=self.request.path.split('/')[-2])
        form.instance.post = post
        if form.is_valid():
            form.save()
        return redirect(request.META.get('HTTP_REFERER'))

class AccountView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account.html'
    context_object_name = 'user'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['query_set_posts'] = self.request.user.posts.all().order_by('-id')
        print(not self.request.user.groups.filter(name='Subscribers').exists())
        if not self.request.user.groups.filter(name='Subscribers').exists():
            context['user_is_not_subscribe'] = True
        else:
            context['user_is_not_subscribe'] = False
        return context

def show_banner(request):
    user = request.user
    return user

def subscribe(request, **kwargs):
    user = request.user
    subscribers = Group.objects.get(name='Subscribers')
    if not request.user.groups.filter(name='Subscribers').exists():
        subscribers.user_set.add(user)
        print(request.user.groups.all())
    return redirect(request.META.get('HTTP_REFERER'))





