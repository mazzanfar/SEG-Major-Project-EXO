from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Children
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
# from .forms import ChildrenRegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.apps import apps

Timeline = apps.get_model("timeline", "Timeline")

def home(request):
    context = {
        'children': Children.objects.all()
    }

    return render(request, 'children/children_list.html')

class ChildrenListView(ListView):
    model = Children
    # template_name = 'children/children_list.html'
    context_object_name = 'children'
    # ordering = ['-date_added']

class ChildrenDetailView(DetailView):
    model = Children

class ChildrenCreateView(LoginRequiredMixin,  CreateView):
    model = Children
    fields = ['first_name', 'last_name', 'age', 'disabilities']

    def form_valid(self, form):
        form.instance.parent = self.request.user
        self.object = form.save(commit=False)
        self.object.save()
        timeline = Timeline()
        timeline.child = self.object
        timeline.save()
        for disability in form.cleaned_data['disabilities'].all():
            for c in disability.content.all():
                print(c.title)
                timeline.content.add(c)
        return super().form_valid(form)

class ChildrenUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Children
    fields = ['first_name', 'last_name', 'age', 'disabilities']

    def form_valid(self, form):
        form.instance.parent = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        child = self.get_object()
        if self.request.user == child.parent:
            return True 
        return False

class ChildrenDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Children
    success_url = '/'

    def test_func(self):
        child = self.get_object()
        if self.request.user == child.parent:
            return True 
        return False
