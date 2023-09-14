from django.urls import path
from .views import *

urlpatterns = [
    # path('', cache_page(60)(PostList.as_view()), name='news'),
    # path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('index', PostListView.as_view(), name='posts'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>', PostsByCategoryView.as_view(), name='posts_by_categories'),
    path('<int:pk>/add_comment', CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/account', AccountView.as_view(), name='account'),
    path('<int:pk>/account/comments', CommentListView.as_view(), name='comments'),
    path('<int:pk>/account/add_post', PostCreateView.as_view(), name='add_post'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='edit_post'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='delete_post'),
    path('<int:pk>/account/subscribe', subscribe, name='subscribe'),

]