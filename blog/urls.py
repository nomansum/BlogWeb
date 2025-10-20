from django.urls import path
from .views import CategoryList, PostListCreate, PostDetail, CommentListCreate, CommentDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]