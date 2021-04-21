from django.urls import path
from memberships.api.views import api_plans_view


urlpatterns = [
    path('', api_plans_view, name='api_plans'),
]