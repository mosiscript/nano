from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from jalali_date import datetime2jalali, date2jalali
from .models import Article


def published_fa(model):
    return datetime2jalali(model.published_at).strftime('%y/%m/%d _ %H:%M:%S')

published_fa.short_description = 'زمان انتشار'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin, ModelAdminJalaliMixin):
    list_display = ('title', 'view', published_fa, 'show')
    date_hierarchy = 'published_at'
    search_fields = ('title', 'body')
    list_filter = ('published_at', )
    ordering = ['published_at']
    actions = ['make_hide', 'make_show']

    fieldsets = (
        ('section 1' , {
            'fields' : ('title', 'body', 'published_at')
        }),
        ('موارد بیشتر ' , {
            'classes' : ('collapse', ) ,
            'fields' : ('view', 'show')
        })
    )

    def make_hide(self, request, queryset):
        row_updated = queryset.update(show = 0)
        self.giveMessage(request, row_updated, 'hide')

    make_hide.short_description = 'Make selected articles as hide'



    def make_show(self, request, queryset):
        row_updated = queryset.update(show = 1)
        self.giveMessage(request, row_updated, 'show')

    make_show.short_description = 'Make selected articles as show'

    def giveMessage(self, request, row_updated, type):
        if(row_updated == 1):
            message_bit = '1 article was'
        else:
            message_bit = '%s articles were' % row_updated
        
        self.message_user(request, '%s successfully marked as %s' % (message_bit, type))

