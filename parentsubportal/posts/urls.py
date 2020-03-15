from django.urls import path
from rest_framework import routers
from .api import (
    TopicViewSet, 
    PostViewSet, 
    CommentViewSet,
    RatingViewSet,
    PDFViewSet
)

router = routers.DefaultRouter()
router.register('api/topics', TopicViewSet, 'topics')
router.register('api/comments', CommentViewSet, 'comments')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/comments', CommentViewSet, 'comments')
router.register('api/ratings', RatingViewSet, 'ratings')
router.register('api/pdfs', PDFViewSet, 'pdfs')
#router.register('api/comments/saveComment')

urlpatterns = router.urls
