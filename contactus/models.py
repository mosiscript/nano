from django.db import models
from django.utils import timezone

class Contactus(models.Model):
    subject = models.CharField(max_length=100, verbose_name='موضوع')
    message = models.TextField(max_length=1000, blank=True, null=True, verbose_name='پیام')
    sender = models.EmailField(verbose_name='ایمیل')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='زمان قرارگیری')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس ها'

    def __str__(self):
        return self.subject
