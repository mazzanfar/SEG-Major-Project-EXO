from django.db import models
from taggit.managers import TaggableManager


class HealthCondition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    url = models.URLField()
    published = models.BooleanField(default=False)
    keywords = TaggableManager()

    def __str__(self):
        return self.name


class HealthInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    url = models.URLField()
    keywords = TaggableManager()
    health_condition_id = models.ForeignKey(
        'HealthCondition', related_name='infos', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PageLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, null=True)
    url = models.URLField()
    published = models.BooleanField(default=False)
    description = models.TextField(null=True)
    title = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=False)
    keywords = TaggableManager()

    def __str__(self):
        return self.name
