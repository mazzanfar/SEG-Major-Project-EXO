from django.db import models

# Create your models here.
class News(models.Model):
    #image and description for each news
    images = models.ImageField(upload_to='images/')
    description = models.CharField(max_length = 500)
