from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='page_index'),
    path('details/', views.details, name='page_details'),
    path('create/', views.create, name='page_create'),
    path('update/<int:pk>', views.update, name='page_update'),
    path('delete/<int:pk>', views.delete, name='page_delete'),
]