from django.db import models
from django.utils import timezone

class Subscribe(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    date = models.DateTimeField(default=timezone.now, verbose_name='زمان ارسال')

    class Meta:
        verbose_name = 'اشتراک'
        verbose_name_plural = 'اشتراک ها'

    def __str__(self):
        return self.title