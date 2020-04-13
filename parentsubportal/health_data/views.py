from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UrlForm
from .data_fetch.crawler import scrape
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required
def healthData_page(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            pdfs = scrape(request.POST['url'])
            return render(request, 'health_data/healthData_page.html', {'form': form, 'pdfs': pdfs})

    else:
        print("called 1")
        form = UrlForm()

    return render(request, 'health_data/healthData_page.html', {'form': form,})
