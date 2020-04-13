from django.urls import path
from rest_framework import routers
from .api import (
    TopicViewSet, 
    PostViewSet, 
    CommentViewSet,
    RatingViewSet,
    PDFViewSet,
    ResourceViewSet,
    VideoViewSet,
    DisabilityViewSet
)
from children.api import ChildrenViewSet
from timeline.api import TimelineViewSet

router = routers.DefaultRouter()
router.register('api/topics', TopicViewSet, 'topics')
router.register('api/comments', CommentViewSet, 'comments')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/comments', CommentViewSet, 'comments')
router.register('api/ratings', RatingViewSet, 'ratings')
router.register('api/pdfs', PDFViewSet, 'pdfs')
router.register('api/resources', ResourceViewSet, 'resources')
router.register('api/videos', VideoViewSet, 'videos')
router.register('api/children', ChildrenViewSet, 'videos')
router.register('api/disabilities', DisabilityViewSet, 'disabilities')
router.register('api/timelines', TimelineViewSet, 'timelines')
#router.register('api/comments/saveComment')

urlpatterns = router.urls
