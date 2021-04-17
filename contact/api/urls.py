from django.urls import path
from contact.api.views import api_contact_create_view


urlpatterns = [
    path('create', api_contact_create_view, name='api_contact_create'),
]