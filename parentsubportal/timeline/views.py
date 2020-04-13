from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from children.models import Children
from .models import Timeline, Pdf
from .forms import TimelineForm, PdfForm, TimelineToUploadForm
from django.contrib.auth.models import User
from collections import defaultdict
from posts.models import Topic
# Create your views here.

@login_required
def timeline(request):
    user = request.user
    children = user.children.all()
    if request.method == "POST":
        childId = request.POST['child']
        child = children.get(id=childId)
        timeline = child.timeline.get()
        children = user.children.all()
        return render(request, 'timeline.html', {
            'children' : children,
            'group': timeline,
    })
    else: 
        child = user.children.first()
        if (child != None): 
            timeline = child.timeline.get()
            print(timeline.content.all())
        else:
            timeline = None
        return render(request, 'timeline.html', {
        'children' : children,
        'group': timeline,
    })

def upload(request):
    if request.method == 'POST':
        form = TimelineToUploadForm(request.POST, request.FILES)
        form_pdf = PdfForm(request.POST, request.FILES)
        if form.is_valid() and form_pdf.is_valid():
            header = form.cleaned_data['header']
            age = form.cleaned_data['age']
            child = form.cleaned_data['child']
            search_result = Timeline.objects.get(header = header, age = age, child = child)
            form_pdf.instance.timeline = search_result
            form_pdf.save()
            return redirect('timeline')
    else:
        form = TimelineForm(request.user)
        form_pdf = PdfForm()
    return render(request, 'upload.html', {
        'form': form,
        'form_pdf': form_pdf
    })

def my_children(request, *args, **kwargs):
    user = request.user
    form = TimelineForm(user)
