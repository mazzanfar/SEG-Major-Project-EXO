"""parentsubportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from users import views as user_views
from pages import views as pages_views
from frontend import views as views
from timeline import views as timeline_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', pages_views.home_page, name="home_page"),
    #path('welcome_page/', pages_views.welcome_page, name="welcome_page"),
    #path('welcome_page2/', pages_views.welcome_page2, name="welcome_page2"),
    path('blogs/', pages_views.blogs_page, name="blogs_page"),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('add_children/', user_views.addChild, name='children_form'),
    path('timeline/', timeline_views.timeline, name='timeline'),
    path('upload/', timeline_views.upload_pdf, name = 'upload'),
    path('', include('frontend.urls')),
    path('', include('posts.urls')),
    path('', include('users.urls')),
    re_path('.*', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
