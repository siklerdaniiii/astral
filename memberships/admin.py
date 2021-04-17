from django.contrib import admin
from .models import Plan ,Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ['member_name', 'member_email', 'member_uid', 'member_plan', 'member_status','member_since', 'member_expires']
admin.site.register(Member, MemberAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan_name', 'plan_slug', 'plan_price', 'plan_length', 'plan_status']
admin.site.register(Plan, PlanAdmin)
