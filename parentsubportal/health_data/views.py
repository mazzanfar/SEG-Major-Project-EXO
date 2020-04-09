from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UrlForm
from .data_fetch.crawler import scrape
import pdb


def healthData_page(request):
    
    if request.method == 'POST':
        pdb.set_trace()
        form = UrlForm(request.POST)
        if form.is_valid():
            scrape(request.POST['url'])
            return HttpResponseRedirect('')

    else:
        print("called 1")
        form = UrlForm()

    return render(request, 'health_data/healthData_page.html', {'form': form})
