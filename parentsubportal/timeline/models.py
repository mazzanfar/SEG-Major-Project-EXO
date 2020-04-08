from django.db import models
from django.contrib.auth.models import User
from posts.models import PDF
from children.models import Children

HEADER_CHOICES = [
    ('Financial Support', 'Financial Support'),
    ('Educational Support', 'Educational Support'),
    ('Governmental Support', 'Governmental Support '),
    ('Charity Support Groups', 'Charity Support Groups'),
    ('Therapy Support', 'Therapy Support '),
    ('Transport Support', 'Transport Support ')
]
AGE_CHOICES = [
    ('0-4', '0-4'),
    ('4-11', '4-11'),
    ('11-18', '11-18'),
    ('18-25', '18-25')
]

class Timeline(models.Model):
    header = models.CharField(max_length=30, choices=HEADER_CHOICES)
    age = models.CharField(max_length=6, choices=AGE_CHOICES)
    child = models.OneToOneField(Children, on_delete=models.CASCADE)

class Pdf(models.Model):
    pdf = models.FileField(upload_to='timelinepdfs')
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
