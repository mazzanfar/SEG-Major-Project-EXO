from django.urls import path
from .views import PostListView, CreateListView, PostDetailView, PostsListByTopicView, CommentListView

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path("topic/<str:name>/", PostsListByTopicView.as_view(), name="topic"),
    path("comments/", CommentListView.as_view(), name="comments"),
]
