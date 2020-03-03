from rest_framework import serializers
from .models import Topic

# Lead Serializer
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
