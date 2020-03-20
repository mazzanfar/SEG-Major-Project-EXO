from django.db import models
from django.contrib.auth.models import User
from users import models as user_models


class Pdfs (models.Model):
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to = 'timeline/pdfs/')

    def __str__(self):
        return self.name

class Timeline(models.Model):
    title = models.CharField(max_length=100)
    ageRange = models.CharField(max_length=100)
    pdf = models.ForeignKey('Pdfs', default = None)
    child = user_models.Children.ForeignKey(user_models.Children, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def save(self):
        

# Create your models here.

