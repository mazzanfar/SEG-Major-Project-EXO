from django.db import models
from django.db.models import Sum
from django.core.files import File
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from django.db.models import Sum
from model_utils.managers import InheritanceManager

AGE_GROUP_CHOICES = (
        ("0-4", "0-4"),
        ("4-11", "4-11"),
        ("11-18", "11-18"),
        ("18-25", "18-25"),
        ("N/A", "N/A")
    )

class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name

class Disability(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(blank=True, max_length=400)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Disabilities"

    def __str__(self):
        return self.name
    
class Content(models.Model):
    objects = InheritanceManager()
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s", blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    topics = models.ManyToManyField(Topic, null=True, related_name="topics")
    disabilities = models.ManyToManyField(Disability, null=True, blank=True, related_name="content")
    visible = models.BooleanField(default=True)
    age_group = models.CharField(
            max_length=20,
            choices=AGE_GROUP_CHOICES,
            default = "N/A",
            )

    class Meta:
        ordering=['-date_posted']

    def avg_rating(self):
        if self.ratings.count() == 0:
            return 0
        else:
            return self.ratings.aggregate(sum=Sum('rating'))['sum']

    # def likes_count(self):
    #     return sum(v.vote_type == "like" for v in self.post_likes.all())

    # def dislikes_count(self):
    #    return sum(v.vote_type == "dislike" for v in self.post_likes.all())

    def is_negative_post(self):
        """Returns whether the post has more likes than dislikes (min 10 votes)"""
        return True

    @property
    def total_comments(self):
        return self.comments.count()

    @property
    def tidy_date(self):
        return self.date_posted.strftime("%d %b, %Y, %H:%M %p") 

    @property
    def total_likes(self):
        return self.likes.count()

class Post(Content):
    @property
    def get_url(self):
        return "/posts/" + str(self.id)

class Resource(Content):
    source = models.URLField(blank=True)

    class Meta:
        abstract = True

class PDF(Resource):
    pdf_file = models.FileField(upload_to=f'resources/pdfs', null=False, blank=False)

    @property
    def get_url(self):
        return "/pdfs/" + str(self.id)

class Video(Resource):
    videoId = models.CharField(max_length=150, blank=False)

    @property
    def get_url(self):
        return "/posts/" + str(self.id)

class Rating(models.Model):
    content = models.ForeignKey(Content, related_name="ratings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="ratings", on_delete=models.CASCADE)
    rating  = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = [('user', 'content')]

class Comment(models.Model):
    #uid = models.UUIDField(max_length=8, primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    #modified_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    #parent = TreeForeignKey('self', blank=True, related_name='children', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.username, self.post.title)

    @property
    def tidy_date(self):
        return self.created_on.strftime("%d %b, %Y, %H:%M %p") 

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.post.pk}) #TODO: remove 'posts:'
