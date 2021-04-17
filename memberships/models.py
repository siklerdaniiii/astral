from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Vázlat"),
    (1,"Publikálva")
)

MEMBER_STATUS = (
    (0,"Inaktív"),
    (1,"Aktív")
)

PLAN_SLUG = (
    ("free","free"),
    ("plan_1","plan_1"),
    ("plan_2","plan_2"),
    ("plan_3","plan_3"),
    ("plan_4","plan_4"),
    ("plan_5","plan_5")
)


class Plan(models.Model):
    plan_name = models.CharField(max_length=200, unique=True)
    plan_slug = models.CharField(choices=PLAN_SLUG, max_length=200, default='free', unique=True)
    plan_description = models.TextField()
    plan_length = models.IntegerField(default=1)#day
    plan_price = models.IntegerField(default=0)
    plan_image = models.ImageField(upload_to='plans', default='plans/default.jpg')
    plan_status = models.IntegerField(choices=STATUS, default=0)
    plan_updated_at = models.DateTimeField(auto_now= True)
    plan_created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-plan_created_at']

    def __str__(self):
        return self.plan_name



class Member(models.Model):
    member_email = models.CharField(max_length=200)
    member_uid = models.CharField(max_length=254)
    member_status = models.IntegerField(choices=MEMBER_STATUS, default=0)
    member_plan = models.ForeignKey(Plan, on_delete=models.SET_NULL,related_name='members_plans', null=True, blank=True)
    member_since =  models.DateField(auto_now=False, auto_now_add=False)
    member_expires = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.member_email


