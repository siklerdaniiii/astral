from django.urls import path
from blog.api.views import api_blog_view, api_blog_details_view, api_blog_by_category_view, api_blog_categories_view


urlpatterns = [
    path('', api_blog_view, name='api_blog'),
    path('<pk>/', api_blog_details_view, name='api_blog_details'),
    path('category/<pk>/', api_blog_by_category_view, name='api_blog_by_category'),
    path('category', api_blog_categories_view, name='api_blog_categories'),
]