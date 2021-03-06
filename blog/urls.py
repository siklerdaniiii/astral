from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('details/', views.details, name='blog_details'),
    path('create/', views.create, name='blog_create'),
    path('update/<int:pk>', views.update, name='blog_update'),
    path('delete/<int:pk>', views.delete, name='blog_delete'),

    path('categories', views.index_category, name='blog_category_index'),
    path('category/details/', views.details_category, name='blog_category_details'),
    path('category/create/', views.create_category, name='blog_category_create'),
    path('category/update/<int:pk>', views.update_category, name='blog_category_update'),
    path('category/delete/<int:pk>', views.delete_category, name='blog_category_delete'),


    path('owners', views.index_owner, name='blog_owner_index'),
    path('owner/details/', views.details_owner, name='blog_owner_details'),
    path('owner/create/', views.create_owner, name='blog_owner_create'),
    path('owner/update/<int:pk>', views.update_owner, name='blog_owner_update'),
    path('owner/delete/<int:pk>', views.delete_owner, name='blog_owner_delete'),
]