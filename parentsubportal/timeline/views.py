from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required

from .models import Timeline, Pdf
from .forms import TimelineForm, PdfForm
=======
from .forms import TimelineForm
from .models import Timeline
from django.contrib.auth.decorators import login_required
>>>>>>> timeline
# Create your views here.

@login_required
def timeline(request):
    timeline = Timeline.objects.all()
    return render(request, 'timeline.html', {
        'timeline': timeline
    })

<<<<<<< HEAD
def upload(request):
    if request.method == 'POST':
        form = TimelineForm(request.POST, request.FILES)
        form_pdf = PdfForm(request.POST, request.FILES)
        if form.is_valid() and form_pdf.is_valid():
            timeline = form.save()
            form_pdf.instance.timeline = timeline
            form_pdf.save()
            return redirect('timelinelist.html')
    else:
        form = TimelineForm()
        form_pdf = PdfForm()
    return render(request, 'upload.html', {
        'form': form,
        'form_pdf': form_pdf
    })
=======
def upload_pdf(request):
    if request.method == 'POST':
        form = TimelineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeline.html')
    
    else:
        form = TimelineForm()
    return render(request, 'upload_pdf.html',{
        'form': form
    })
>>>>>>> timeline
