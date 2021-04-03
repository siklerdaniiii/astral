from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Account
from accounts.api.serializers import AccountApi



@api_view(['GET',])
def api_accounts_view(request):
    try:
        account = Account.objects.all()#filter(post_status = 1)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountApi(account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST',])
def api_accounts_create_view(request):
    if request.method == 'POST':
        serializer = AccountApi(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



