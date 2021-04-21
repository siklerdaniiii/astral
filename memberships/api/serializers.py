from rest_framework import  serializers
from memberships.models import Plan


class PlanApi(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = "__all__"




