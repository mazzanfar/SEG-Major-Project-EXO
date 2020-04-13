from django.db import models
from django.contrib.auth.models import User
from children.models import Children
from posts.models import Topic, Content, Resource
from collections import defaultdict


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
    header = models.CharField(max_length=30, choices=HEADER_CHOICES, blank=True)
    age = models.CharField(max_length=6, choices=AGE_CHOICES, blank=True)
    child = models.ForeignKey(Children, on_delete=models.CASCADE, related_name="timeline")
    content = models.ManyToManyField(Content, null=True, blank=True, related_name="contents")

    """ Returns a dictionary of pdfs sorted by age group, then topic"""
    @property
    def get_sorted_pdfs(self):
        age_groups = defaultdict(list, { k:[] for k in ('0-4', '4-11', '11-18', '18-25', 'N/A',)})
        for c in self.content.all().select_subclasses():
            age_groups[c.age_group].append(c)
        group = {} 
        for k, v in age_groups.items():
            group[k] = {}
            for c in v:
                for topic in c.topics.all():
                    if not topic.name in group:
                        group[k][topic.name] = [c]
                    else:
                        group[k][topic.name].append(c)
        return group

class Pdf(models.Model):
    pdf = models.FileField(upload_to='timelinepdfs')
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
