from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact_index'),
    path('details/<int:pk>', views.details, name='contact_details'),
    path('update/<int:pk>', views.update, name='contact_update'),
    path('delete/<int:pk>', views.delete, name='contact_delete'),

]