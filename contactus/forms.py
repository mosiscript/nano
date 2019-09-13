from django import forms
from .models import Contactus

class ContactusForm(forms.Form):
    subject = forms.CharField(min_length=3, max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
