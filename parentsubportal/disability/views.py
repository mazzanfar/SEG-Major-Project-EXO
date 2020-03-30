from django.shortcuts import render
from .models import Disability
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# Create your views here.

class disability_detail(ListView):
    model = Disability
    template_name = 'disability/disability_detail.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Disability.objects.filter(
            Q(keywords__icontains=query) | Q(name__icontains=query)
        )
        return object_list

class search_view(TemplateView):
    model = Disability
    template_name = 'disability/search.html'

    def get_queryset(self):
        object_list = Disability.objects.all()[:1].get()
        return object_list
    