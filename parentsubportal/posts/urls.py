from django.urls import path
from rest_framework import routers
from .api import (
    TopicViewSet, 
    PostViewSet, 
    DocumentViewSet, 
    CommentViewSet,
    LikeViewSet
)

router = routers.DefaultRouter()
router.register('api/topics', TopicViewSet, 'topics')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/documents', DocumentViewSet, 'documents')
router.register('api/comments', CommentViewSet, 'comments')
router.register('api/likes', LikeViewSet, 'likes')
#router.register('api/comments/saveComment')

urlpatterns = router.urls
