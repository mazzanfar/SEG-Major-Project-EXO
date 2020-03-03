from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    news = News.objects
    return render(request, 'pages/welcome_page.html')

def welcome_page2(request):
    return render(request, 'pages/welcome_page2.html')

def home_page(request):
    return render(request, 'pages/home_page.html')

def blogs_page(request):
    return render(request, 'pages/blogs_page.html')
