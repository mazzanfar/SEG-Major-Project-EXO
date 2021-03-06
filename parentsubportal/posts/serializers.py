from rest_framework import serializers
from itertools import chain
from .models import (
    Topic, 
    Post, 
    Comment, 
    Rating,
    PDF,
    Content,
    Video,
    Disability,
)

class DisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disability
        fields = '__all__'

class ResourceSerializer(serializers.Serializer):
    pass

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
    tidy_date = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "content", "author", "post", "tidy_date"]

class PDFSerializer(serializers.ModelSerializer):
    total_comments = serializers.IntegerField(read_only=True)
    tidy_date = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    author_username = serializers.CharField(source="author.username", read_only=True)
    topic_names = TopicSerializer(many=True, read_only=True, source='topics')
    avg_rating = serializers.FloatField(read_only=True)
    disability_names = DisabilitySerializer(many=True, read_only=True, source='disabilities')

    def get_rating(self, obj):
        r = obj.post_ratings.filter(user=requestUser).first()
        if (r is not None):
            return r.rating
        return None

    class Meta:
        model = PDF
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    total_comments = serializers.IntegerField(read_only=True)
    tidy_date = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    author_username = serializers.CharField(source="author.username", read_only=True)
    topic_names = TopicSerializer(many=True, read_only=True, source='topics')
    avg_rating = serializers.FloatField(read_only=True)
    disability_names = DisabilitySerializer(many=True, read_only=True, source='disabilities')

    class Meta:
        model = Video
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    """DRF serializer listing all the posts"""
    total_comments = serializers.IntegerField(read_only=True)
    tidy_date = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    author_username = serializers.CharField(source="author.username", read_only=True)
    topic_names = TopicSerializer(many=True, read_only=True, source='topics')
    avg_rating = serializers.FloatField(read_only=True)
    disability_names = DisabilitySerializer(many=True, read_only=True, source='disabilities')

    class Meta:
        model = Post
        fields = '__all__'

    def get_queryset(self):
        queryset = Post.objects.all()
        topic = self.request.query_params.get('topic', None)
        if queryset is not None:
            queryset = queryset.filter(topics__id[topic])

        return queryset

    def get_rating(self, obj):
        r = obj.post_ratings.filter(user=requestUser).first()
        if (r is not None):
            return r.rating
        return None

class PostDetailSerializer(serializers.ModelSerializer):
    """DRF serializer listing details of a blog post"""
    total_comments = serializers.IntegerField()
    comments_list = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'total_comments', 'comments_list']
