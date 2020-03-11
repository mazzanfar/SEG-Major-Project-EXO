from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# .........


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=200, default='default')
    address = models.CharField(max_length=200, default='default')
    gender = models.CharField(max_length=20, default='default')
    image = models.ImageField(default='default.jpg', upload_to='profile')
    country = models.CharField(max_length=50, default='default')
    city = models.CharField(max_length=50, default='default')

    def __str__(self):
        return self.user.username

    def save_img(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
