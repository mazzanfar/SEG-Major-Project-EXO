from django.urls import path, include
from .api import UserAPI

urlpatterns = [
    path('api/auth/user', UserAPI.as_view()),
]
