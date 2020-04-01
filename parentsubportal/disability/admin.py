from django.contrib import admin
from .models import Disability, PDFFile, Keyword
# Register your models here.

admin.site.register(Disability)
admin.site.register(PDFFile)
admin.site.register(Keyword)