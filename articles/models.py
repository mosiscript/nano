from django.db import models
from django.utils import timezone
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):

    title = models.CharField(max_length = 100, verbose_name = 'عنوان')
    # body = models.TextField()
    # body = RichTextField(blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    # body = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[('youtube', )])
    view = models.IntegerField(default = 0, verbose_name = 'بازدیدها')
    show = models.BooleanField(default = 1, verbose_name = 'نمایش')
    published_at = models.DateTimeField(default = timezone.now, verbose_name = 'زمان انتشار')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
    
    def __str__(self):
        return self.title

