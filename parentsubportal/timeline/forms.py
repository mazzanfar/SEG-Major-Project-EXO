from django import forms
<<<<<<< HEAD
from .models import Timeline, Pdf
=======
from .models import Timeline
>>>>>>> timeline

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
<<<<<<< HEAD
        fields = ('header', 'age')

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('pdf',)
=======
        fields = ('header','age','pdf')
>>>>>>> timeline
