from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from django.db.models import Q

from memberships.models import Plan
from memberships.api.serializers import PlanApi


@api_view(['GET',])
def api_plans_view(request):
    try:
        plans = Plan.objects.all().exclude(plan_slug = 'free')
    except Plan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlanApi(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
