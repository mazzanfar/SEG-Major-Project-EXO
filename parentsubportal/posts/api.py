from .models import (
    Topic,
    Post, 
    Document, 
    Comment,
    Like
)
from rest_framework import viewsets, permissions
from .serializers import (
    TopicSerializer, 
    PostListSerializer, 
    DocumentSerializer, 
    CommentSerializer,
    LikeSerializer
)

# Votes ViewSet
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LikeSerializer

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

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DocumentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializer
