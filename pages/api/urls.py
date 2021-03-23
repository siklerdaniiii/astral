from django.urls import path
from pages.api.views import api_page_details_view


urlpatterns = [
    path('<pk>', api_page_details_view, name='api_page_details'),
]