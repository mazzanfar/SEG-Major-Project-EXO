from django.shortcuts import render
from .models import Publication, Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

posts = [
    {
        'author' : 'Ryan Bouguerra',
        'title' : 'How it works',
        'content' : 'Welcome to ...',
        'date_added' : '09/03/20'
    },

    {
        'author' : 'Hedi Gharbi',
        'title' : 'Presentation',
        'content' : 'Why use...',
        'date_added' : '09/03/20'
    }
]

publications = [
    {
        'title' : 'Billet eurostar 1',
        'itinerary' : 'Paris-London',
        'date_added' : '09/03/20',
        'username' : 'youssefz1'
    },

    {
        'title' : 'Billet eurostar 2',
        'itinerary' : 'Paris-London',
        'date_added' : '04/03/20',
        'username' : 'mouz99'
    }
]

@login_required
def home(request):
    context = {
        'publications' : Publication.objects.all()
    }
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html', {'title' : 'about'})

class PublicationListView(ListView):
    model = Publication
    template_name = 'store/home.html'
    context_object_name = 'publications'
    ordering = ['-date_added']

class PublicationDetailView(DetailView):
    model = Publication

class PublicationCreateView(LoginRequiredMixin,  CreateView):
    model = Publication
    fields = ['title', 'itinerary']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    
class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publication
    fields = ['title', 'itinerary']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        publication = self.get_object()
        if self.request.user == publication.username:
            return True 
        return False

class PublicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publication
    success_url = '/'

    def test_func(self):
        publication = self.get_object()
        if self.request.user == publication.username:
            return True 
        return False

@login_required
def newest_posts(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'store/newest_posts.html', context)