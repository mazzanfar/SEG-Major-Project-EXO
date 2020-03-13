from django.db import models


class SpiderFetch(models.Model):
    nameOfDisease = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    keyword = models.CharField(max_length=200)

    class Meta:
        verbose_name = "the links"
