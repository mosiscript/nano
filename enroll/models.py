from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone 

class Enroll(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    phone_regex = RegexValidator(regex=r'^(09)\d{9,9}$', message='شماره وارد شده صحیح نیست')
    mobile = models.CharField(validators=[phone_regex], max_length=11)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'ثبت نام'
        verbose_name_plural = 'ثبت نام ها'

    def __str__(self):
        return self.name 
