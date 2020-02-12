from django.shortcuts import render
from .models import News

# Create your views here.
def welcome_page(request):
    news = News.objects
    return render(request, 'welcome_page.html', {'news': news})
