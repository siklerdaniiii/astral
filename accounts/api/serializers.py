from rest_framework import  serializers
from accounts.models import Account

class AccountApi(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

