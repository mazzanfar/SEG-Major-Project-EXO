from django import forms
from .models import Timeline, Pdf
from django.contrib.auth.models import User
from children.views import Children

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = ('header', 'age', 'child')


    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['child'].queryset = Children.objects.filter(parent=user)

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('pdf',)
