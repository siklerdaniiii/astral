from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='post_index'),
    path('x/<uid>', views.index2, name='post_index2'),
    path('details/', views.details, name='post_details'),
    path('create/', views.create, name='post_create'),
    path('update/<int:pk>', views.update, name='post_update'),
    path('delete/<int:pk>', views.delete, name='post_delete'),

    path('owners', views.index_owner, name='post_owner_index'),
    path('owner/details/', views.details_owner, name='post_owner_details'),
    path('owner/create/', views.create_owner, name='post_owner_create'),
    path('owner/update/<int:pk>', views.update_owner, name='post_owner_update'),
    path('owner/delete/<int:pk>', views.delete_owner, name='post_owner_delete'),

    path('categories', views.index_category, name='post_category_index'),
    path('category/details/', views.details_category, name='post_category_details'),
    path('category/create/', views.create_category, name='post_category_create'),
    path('category/update/<int:pk>', views.update_category, name='post_category_update'),
    path('category/delete/<int:pk>', views.delete_category, name='post_category_delete'),
]