from rest_framework import  serializers
from contact.models import Contact

class ContactApi(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

