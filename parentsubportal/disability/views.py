from django.shortcuts import render
from django.db.models import Q
from .models import Disability
from django.views.generic import TemplateView, ListView
# Create your views here.

class HomePageView(TemplateView):
    template_name = "disability/homepage.html"

class SearchResultsView(ListView):
    model = Disability
    template_name = "disability/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = Disability.objects.filter(
            Q(name__icontains = query) | Q(tags__title__icontains = query)
        )

        return object_list