from rest_framework import serializers
from .models import (
    Topic, 
    Post, 
    Comment, 
    Rating,
    PDF
)

# Vote Serializer
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

# Topic Serializer
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "author", "post"]

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'
        #fields = ["content", "author", "title", "source", "content", "topics"]

class PostListSerializer(serializers.ModelSerializer):
    """DRF serializer listing all the posts"""
    total_comments = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    dislikes_count = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    topics = TopicSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    """DRF serializer listing details of a blog post"""
    total_comments = serializers.IntegerField()
    comments_list = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'total_comments', 'comments_list']

