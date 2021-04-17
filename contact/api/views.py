from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from contact.models import Contact
from contact.api.serializers import ContactApi

@api_view(['POST',])
def api_contact_create_view(request):
    if request.method == 'POST':
        serializer = ContactApi(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)