from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from posts.serializers import RatingSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

# User Serializer
class UserSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    user_ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")

