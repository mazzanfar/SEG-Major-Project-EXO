from .models import (
    Topic,
    Post, 
    Comment,
    Rating,
    PDF
)
from rest_framework import viewsets, permissions
from .serializers import (
    TopicSerializer, 
    PostListSerializer, 
    CommentSerializer,
    RatingSerializer,
    PDFSerializer
)

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
