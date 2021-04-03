from django.urls import path
from accounts.api.views import api_accounts_view, api_accounts_create_view


urlpatterns = [
    path('', api_accounts_view, name='api_accounts'),
    path('create', api_accounts_create_view, name='api_accounts_create'),
]