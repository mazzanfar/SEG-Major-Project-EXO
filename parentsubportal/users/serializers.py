from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from posts.serializers import RatingSerializer

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    user_ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_ratings')

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")

