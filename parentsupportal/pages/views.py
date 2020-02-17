from django.shortcuts import render
from .models import News
#from .form import profile_Form

# Create your views here.
def welcome_page(request):
    news = News.objects
    return render(request, 'pages/welcome_page.html', {'news': news})

def welcome_page2(request):
    return render(request, 'pages/welcome_page2.html')
