from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pages.models import Page
from pages.api.serializers import PageApi


@api_view(['GET',])
def api_page_details_view(request, pk):
    try:
        page = Page.objects.get(pk=pk)
    except Page.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PageApi(page)
        return Response(serializer.data, status=status.HTTP_200_OK)

