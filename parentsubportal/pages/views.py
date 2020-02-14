from django.shortcuts import render
from .models import News

# Create your views here.
def welcome_page(request):
    news = News.objects
    return render(request, 'welcome_page.html', {'news': news})

def welcome_page2(request):
    return render(request, 'welcome_page2.html')
