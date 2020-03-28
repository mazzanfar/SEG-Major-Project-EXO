from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey 
from django.core.files import File
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager

class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name
    
class Content(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    topics = models.ManyToManyField(Topic, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def votes_count(self):
        return self.post_ratings.all().count()

    # def likes_count(self):
    #     return sum(v.vote_type == "like" for v in self.post_likes.all())

    # def dislikes_count(self):
    #    return sum(v.vote_type == "dislike" for v in self.post_likes.all())

    def is_negative_post(self):
        """Returns whether the post has more likes than dislikes (min 10 votes)"""
        return True

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.pk}) #TODO: remove 'posts:'

    @property
    def total_comments(self):
        return self.comments.count()

    @property
    def total_likes(self):
        return self.likes.count()

class Post(Content):
    pass

class Resource(Content):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resources", blank=False)
    source = models.URLField(blank=True)
    lower_age = models.IntegerField(blank=True)
    upper_age = models.IntegerField(blank=True)

    class Meta:
        abstract = True

class PDF(Resource):
    pdf_file = models.FileField(upload_to='resources/pdfs/', null=False, blank=False)

class Rating(models.Model):
    post = models.ForeignKey(Post, related_name="post_ratings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_ratings", on_delete=models.CASCADE)
    rating  = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = [('user', 'post')]
    

class Comment(models.Model):
    #uid = models.UUIDField(max_length=8, primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    #modified_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    content = models.TextField()
    #parent = TreeForeignKey('self', blank=True, related_name='children', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.username, self.post.title)

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.post.pk}) #TODO: remove 'posts:'
