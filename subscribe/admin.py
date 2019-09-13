from django.contrib import admin
from .models import Subscribe


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["email", "date" ]
    list_display_links = ["email"]
    list_filter = ["date", "email"]
    search_fields = ('subject', 'email')
    ordering = ['date']
