from django.db import models
from django.contrib.auth.models import User
from users import models as user_models
from posts.models import PDF

class Timeline(models.Model):
    header = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    pdf = models.ManyToManyField(PDF, default = None, related_name="timelines")

    def __str__(self):
        return self.header
