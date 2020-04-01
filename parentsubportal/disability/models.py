from django.db import models

# Create your models here.
class Keyword(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Disability(models.Model):
    name = models.CharField(max_length=100)
    """
    thefile = models.FileField(null = True, blank= True)
    """
    tags = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.name

class PDFFile(models.Model):
    pdffile = models.FileField(null = True, blank=True)
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE, blank=True, null=True)


