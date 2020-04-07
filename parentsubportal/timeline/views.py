from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from children.models import Children
from .models import Timeline, Pdf
from .forms import TimelineForm, PdfForm
# Create your views here.

@login_required
def timeline(request):
    timeline = Timeline.objects.all()
    children = Children.objects.all()
    pdfs = Pdf.objects.all()
    return render(request, 'timeline.html', {
        'timeline': timeline,
        'children' : children,
        'pdfs' :pdfs
    })

def upload(request):
    if request.method == 'POST':
        form = TimelineForm(request.POST, request.FILES)
        form_pdf = PdfForm(request.POST, request.FILES)
        if form.is_valid() and form_pdf.is_valid():
            search_result = Timeline.objects.get(
                Q(header = form.data['header']) & Q(age = form.data['age']) & Q(child = form.data['child'])
            )
            form_pdf.instance.timeline = search_result
            form_pdf.save()
            return redirect('timeline')
    else:
        form = TimelineForm()
        form_pdf = PdfForm()
    return render(request, 'upload.html', {
        'form': form,
        'form_pdf': form_pdf
    })
