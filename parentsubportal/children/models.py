from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.dispatch import receiver
from django.db.models import signals
from posts.models import Disability

class Children(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    disabilities = models.ManyToManyField(Disability, null=True, blank=True, related_name="child_disabilities")
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")

    def __str__(self):
        return self.first_name + " " + self.last_name
 
    def get_absolute_url(self):
        return reverse('children-detail', kwargs={'pk': self.pk})

