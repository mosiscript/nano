from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["title"]
    # list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ'

admin.site.register(Post, PostModelAdmin)
