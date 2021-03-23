from rest_framework import  serializers
from pages.models import Page

class PageApi(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
