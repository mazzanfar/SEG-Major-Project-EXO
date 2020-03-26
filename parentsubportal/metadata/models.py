from django.db import models


class FetchedData(models.Model):
    nameDisease = models.CharField(max_length=200)
    urllink = models.URLField()

    def __str__(self):
        return self.nameDisease
