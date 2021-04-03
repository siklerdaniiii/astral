from django.db import models

# Create your models here.
class Account(models.Model):
    account_uid = models.CharField(max_length=200, unique=True)
    account_email = models.CharField(max_length=200, db_index=True)
    account_updated_at = models.DateTimeField(auto_now= True)
    account_created_at = models.DateTimeField(auto_now_add=True)