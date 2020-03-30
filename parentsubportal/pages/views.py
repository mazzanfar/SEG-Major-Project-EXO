from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'pages/home_page.html')

def blogs_page(request):
    return render(request, 'pages/blogs_page.html')
