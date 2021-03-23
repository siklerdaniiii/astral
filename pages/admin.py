from django.contrib import admin
from .models import Page 

class PageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'page_status','page_created_at')
    list_filter = ("page_status",)
    search_fields = ['page_title', 'page_description']
admin.site.register(Page, PageAdmin)