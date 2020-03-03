from .models import Topic
from rest_framework import viewsets, permissions
from .serializers import TopicSerializer

# Topic Viewset
class TopicViewset(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TopicSerializer
