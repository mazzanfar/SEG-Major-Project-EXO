from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



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
    parent = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Children'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 