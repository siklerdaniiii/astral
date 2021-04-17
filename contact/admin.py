from django.contrib import admin
from .models import Contact 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email','contact_created_at')
    list_filter = ("contact_status",)
    search_fields = ['contact_name', 'contact_email']
admin.site.register(Contact, ContactAdmin)