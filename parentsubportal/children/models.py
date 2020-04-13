from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.dispatch import receiver
from django.db.models import signals

DIAGNOSIS_CHOICES = [
        (1, ("Yes")), 
        (2, ("No"))
]

class Children(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    diagnosis = models.IntegerField(
        choices= DIAGNOSIS_CHOICES,
    )
    disability = models.CharField(max_length=100)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")

    def __str__(self):
        return self.first_name + " " + self.last_name
 
    def get_absolute_url(self):
        return reverse('children-detail', kwargs={'pk': self.pk})

