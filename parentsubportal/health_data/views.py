from django.shortcuts import render

# Create your views here.
def healthData_page(request):
    return render(request, 'health_data/healthData_page.html')
