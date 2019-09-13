from django import forms
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from .models import Enroll

class EnrollForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    # mobile = PhoneNumberField()
    phone_regex = RegexValidator(regex=r'^(09)\d{9,9}$', message='شماره وارد شده صحیح نیست')
    mobile = forms.CharField(validators=[phone_regex], max_length=11)