from .models import (
    Topic,
    Post, 
    Comment,
    Rating,
    PDF,
    Video
)
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from itertools import chain
from .serializers import (
    TopicSerializer, 
    PostListSerializer, 
    CommentSerializer,
    RatingSerializer,
    PDFSerializer,
    VideoSerializer,
    ResourceSerializer
)

class ResourceViewSet(viewsets.ViewSet):
    def get_queryset(self):
        queryset_a = PDF.objects.all()
        queryset_b = Video.objects.all()

        results_list = list(chain(queryset_a, queryset_b))

        #sorted_list = sorted(results_list, key=lambda instance: -instance.date_posted)

        results = list()
        for entry in results_list:
            item_type = entry.__class__.__name__.lower()
            if isinstance(entry, PDF):
                serializer = PDFSerializer(entry)
            if isinstance(entry, Video):
                serializer = VideoSerializer(entry)

            results.append({'type': item_type, 'data': serializer.data})

        return results

    def list(self, request, *args, **kwargs):
        return Response(self.get_queryset())

# Votes ViewSet
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RatingSerializer

# Topic Viewset
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TopicSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostListSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializer

class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PDFSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    permission_classes = [
            permissions.AllowAny
    ]
    serializer_class = VideoSerializer

