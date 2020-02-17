from django.urls import path
from django.views.generic import TemplateView
from .views import (
    PostListView,
    CreateListView,
    PostDetailView,
    PostsListByTopicView,
    CommentListView,
    PostCreateView,
    CommentFormView,
    PostsListByAuthorView
)

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path("topic/<str:name>/", PostsListByTopicView.as_view(), name="topic"),
    path("user/<str:name>/", PostsListByAuthorView.as_view(), name="post-author"),
    path("comments/", CommentListView.as_view(), name="comments"),
    path("reply_comment/<str:pk>/", CommentFormView.as_view(), name='reply-comment'),
    #path("reply_comment/<int:pk><str:pk2>/", CommentFormView.as_view(), name="reply-comment"),
]
