from django.forms import ModelForm, Textarea, TextInput
from .models import Post, Comment
# from allauth.account.forms import SignupForm
# from django.contrib.auth.models import Group

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['category', 'title', 'text', 'image', 'media_content']
        widgets = {
            'title': TextInput(attrs={'placeholder':'enter post title'}),
            'text': Textarea(attrs={'placeholder':'enter post text', 'cols': 95, 'rows': 10}),
        }

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'placeholder':'enter post text', 'cols': 95, 'rows': 10}),
        }
