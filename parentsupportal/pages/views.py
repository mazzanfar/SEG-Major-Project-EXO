from django.shortcuts import render
from .models import News

# # Create your views here.
# def welcome_page(request):
#     news = News.objects
#     return render(request, 'pages/welcome_page.html', {'news': news})

def home_page(request):
    return render(request, 'pages/home_page.html')

def search_page(request):
    return render(request, 'pages/search_page.html')

def search_page2(request):
    return render(request, 'pages/search_page2.html')
