from django.contrib import admin
from .models import Post ,PostCategory, PostOwner

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['post_category_name']
admin.site.register(PostCategory, CategoryAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ['post_owner_name']
admin.site.register(PostOwner, OwnerAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_status','post_created_at')
    list_filter = ("post_status",)
    search_fields = ['post_title', 'post_description']
admin.site.register(Post, PostAdmin)