from django import forms
from .models import Timeline, Pdf

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = ('header', 'age')

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('pdf',)
