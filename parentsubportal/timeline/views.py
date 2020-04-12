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
    timeline = Timeline.objects.all()
    children = Children.objects.all()
    timelineTest = Timeline.objects.last().content.all().select_subclasses()
    pdfs = Pdf.objects.all()
    age_groups = defaultdict(list)
    for c in timelineTest:
        age_groups[c.age_group].append(c)
    group = {} 
    for k, v in age_groups.items():
        group[k] = {}
        for c in v:
            for topic in c.topics.all():
                if not topic.name in group:
                    group[k][topic.name] = [c]
                else:
                    group[k][topic.name].append(c)

    return render(request, 'timeline.html', {
        'timeline': timeline,
        'children' : children,
        'pdfs' :pdfs,
        'group': group

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
