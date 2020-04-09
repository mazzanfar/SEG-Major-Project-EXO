from rest_framework import serializers
from .models import Children

class ChildrenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Children
        fields = '__all__'
