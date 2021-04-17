from django.contrib import admin
from .models import Blog 

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_status','blog_created_at')
    list_filter = ("blog_status",)
    search_fields = ['blog_title']
admin.site.register(Blog, BlogAdmin)