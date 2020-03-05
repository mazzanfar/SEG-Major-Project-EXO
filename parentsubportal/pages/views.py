from django.shortcuts import render
from .models import News

# Create your views here.
def welcome_page(request):
    news = News.objects
    return render(request, 'pages/welcome_page.html', {'news': news})

def welcome_page2(request):
    return render(request, 'pages/welcome_page2.html')

def home_page(request):
    return render(request, 'pages/home_page.html')

def blogs_page(request):
    return render(request, 'pages/blogs_page.html')
