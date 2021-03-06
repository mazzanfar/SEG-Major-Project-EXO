from django.contrib import admin
from .models import (
    Post,
    Topic, 
    Comment, 
    PDF,
    Rating,
    Disability,
    Video
)

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(PDF)
admin.site.register(Rating)
admin.site.register(Video)
admin.site.register(Disability)
