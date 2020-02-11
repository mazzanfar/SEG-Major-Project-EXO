from django.db import models
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
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.BigIntegerField(default=0)
    topic = models.ManyToManyField(Topic, blank=True)
    #tags = TaggableManager()

    def __str__(self):
        return '{} by {} on {}'.format(self.title, self.author.username, self.date_posted)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    modified_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    content = models.TextField()
    parent = TreeForeignKey('self', blank=True, related_name='children', null=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['created_on']
    
   #  @property
   #  def post(self): #TODO: post should be stored in comment
   #      post = self
   #      while post.parent:
   #          post = post.parent
   #      return Post.objects.get(op=post)

    def getReplies(self):
        replies = Comment.objects.filter(parent=self)
        for reply in replies:
            replies |= reply.getReplies()
        return replies

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.username, self.post.title)

