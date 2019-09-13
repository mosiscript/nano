from django.contrib import admin
from .models import Enroll


@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ["name", "email","mobile", "created_at" ]
    list_display_links = ["name"]
    list_filter = ["created_at", "mobile"]
    search_fields = ('name', 'email', 'mobile')
    ordering = ['created_at']