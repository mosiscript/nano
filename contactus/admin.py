from django.contrib import admin
from .models import Contactus


@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ["subject", "message","sender", "created_at" ]
    list_display_links = ["subject"]
    list_filter = ["created_at", "sender"]
    search_fields = ('subject', 'message', 'sender')
    ordering = ['created_at']
