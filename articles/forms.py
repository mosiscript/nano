from django import forms
from django.core.exceptions import ValidationError
import datetime

class SendAticleForm(forms.Form):
    # title = forms.CharField( min_length = 3, max_length = 50, required = False)
    title = forms.CharField( min_length = 3, max_length = 50, error_messages = {'required':'وارد کردن عنوان الزامی است '})
    body = forms.CharField( widget = forms.Textarea )
    published_at = forms.DateField()

    # title.widget.attrs['class'] = 'form-control'

    def clean_published_at(self):
        date = self.cleaned_data['published_at']

        if date >= datetime.date.today():
            raise ValidationError('تاریخ نباید بزرگتر از زمان امروز باشد')

        return date
