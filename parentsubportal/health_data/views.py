from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UrlForm
from .data_fetch.crawler import scrape


def healthData_page(request):
    if request.method == 'GET':
        form = UrlForm(request.GET)

        if form.is_valid():
            print("called ")
            scrape(UrlForm)
            return HttpResponseRedirect('')

    else:
        form = UrlForm()

    return render(request, 'health_data/healthData_page.html', {'form': form})
