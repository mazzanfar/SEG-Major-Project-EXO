from .models import (
        Children
)
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from itertools import chain
from .serializers import (
        ChildrenSerializer
)

class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = Children.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ChildrenSerializer

