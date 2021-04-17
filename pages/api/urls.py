from django.urls import path
from pages.api.views import api_pages_view


urlpatterns = [
    path('', api_pages_view, name='api_pages'),
]