from django.urls import path
#from .views import PostListView, CreateListView, PostDetailView, PostsListByTopicView, CommentListView

from rest_framework import routers
from .api import TopicViewSet, PostViewSet, DocumentViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/topics', TopicViewSet, 'topics')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/documents', DocumentViewSet, 'documents')
router.register('api/comments', CommentViewSet, 'comments')
#router.register('api/comments/saveComment')

urlpatterns = router.urls
