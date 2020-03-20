from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import TimelineForm
from .models import Timeline
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def timeline_contents(request):
    timeline = Timeline.objects.all()
    return render(request, 'timeline.html', {
        'timeline': timeline
    })

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
