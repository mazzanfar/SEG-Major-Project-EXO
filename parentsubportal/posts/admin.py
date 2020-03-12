from django.contrib import admin
from .models import (
    Post,
    Topic, 
    Comment, 
    Document,
    Like
)

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Document)
admin.site.register(Like)
