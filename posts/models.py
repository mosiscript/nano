from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField



def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True, null=True)
    image = models.ImageField(upload_to=upload_location,
     blank=True,
     null=True,
     height_field="height_field",
     width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    # content = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/posts/%s/' %(self.id)
        # return reverse('posts:post_detail', kwargs={'id': self.id})
        # return reverse('posts:post_detail', kwargs={'slug': self.slug})
    class Meta:
        ordering = ["-timestamp", "-updated"]



# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = slug_new
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
# pre_save.connect(pre_save_post_receiver, sender=Post)
