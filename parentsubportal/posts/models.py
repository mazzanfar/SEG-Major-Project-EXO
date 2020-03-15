import uuid
from django.db import models
from django.core.files import File
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager

class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True)
    topic = models.ManyToManyField(Topic, blank=True)

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.pk}) #TODO: remove 'posts:'

    @property
    def total_comments(self):
        return self.comments.count()

    @property
    def total_likes(self):
        return self.likes.count()

class Document(Post):
    file = models.FileField(upload_to='pdfs', blank=False) 
    

class Comment(models.Model):
    #uid = models.UUIDField(max_length=8, primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    #modified_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    content = models.TextField()
    #parent = TreeForeignKey('self', blank=True, related_name='children', null=True, on_delete=models.CASCADE)

    #class Meta:
        #ordering = ['created_on']
    
   #  @property
   #  def post(self): #TODO: post should be stored in comment
   #      post = self
   #      while post.parent:
   #          post = post.parent
   #      return Post.objects.get(op=post)


    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.username, self.post.title)

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.post.pk}) #TODO: remove 'posts:'
