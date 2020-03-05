from rest_framework import serializers
from .models import Topic, Post, Comment, Document


# Topic Serializer
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "author", "post"]

class PostListSerializer(serializers.ModelSerializer):
    """DRF serializer listing all the posts"""
    total_comments = serializers.IntegerField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    """DRF serializer listing all the documents"""

    class Meta:
        model = Document
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    """DRF serializer listing details of a blog post"""
    total_comments = serializers.IntegerField()
    comments_list = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'total_comments', 'comments_list']

