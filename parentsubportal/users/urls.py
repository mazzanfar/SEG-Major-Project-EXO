from django.urls import path, include
from .api import UserAPI
from knox import views as knox_views

urlpatterns = [
    path('api/auth/user', UserAPI.as_view()),
]
