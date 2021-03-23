from django.urls import path
from posts.api.views import api_posts_view, api_post_details_view, api_post_by_category_view, api_post_by_owner_view, api_post_categories_view, api_post_owners_view


urlpatterns = [
    path('', api_posts_view, name='api_posts'),
    path('<pk>/', api_post_details_view, name='api_post_details'),
    path('category/<pk>/', api_post_by_category_view, name='api_post_by_category'),
    path('owner/<pk>/', api_post_by_owner_view, name='api_post_by_owner'),

    path('category', api_post_categories_view, name='api_post_categories'),
    path('owners', api_post_owners_view, name='api_post_owners'),
]