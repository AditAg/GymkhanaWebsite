from django import forms
from .models import EmailForm

class EmailForm(forms.Form):
    class Meta:
        model=EmailForm
        fields=['firstname','lastname','email','subject','botcheck','message']