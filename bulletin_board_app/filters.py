from django_filters import FilterSet

from .models import Comment, Post

class CommentFilter(FilterSet):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CommentFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(author=self.user)

    class Meta:
        model = Comment
        fields = {
            'post': ['exact'],
        }