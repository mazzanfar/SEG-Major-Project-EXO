from .models import (
        Timeline
)
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from itertools import chain
from .serializers import (
    TimelineSerializer
)

class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TimelineSerializer


