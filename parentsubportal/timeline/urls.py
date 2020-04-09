from django.urls import include, path
from . import views

urlpatterns = [
    path('ajax/load-children/', views.load_children, name='ajax_load_children'),  
]