from django.urls import path
from . import views

urlpatterns = [
    path('plan', views.plan_index, name='plan_index'),
    path('plan/create/', views.plan_create, name='plan_create'),
    path('plan/update/<int:pk>', views.plan_update, name='plan_update'),
    path('plan/delete/<int:pk>', views.plan_delete, name='plan_delete'),

    path('', views.member_index, name='member_index'),
    path('create/', views.member_create, name='member_create'),
    path('update/<int:pk>', views.member_update, name='member_update'),
    path('delete/<int:pk>', views.member_delete, name='member_delete'),

    path('payment', views.payment, name='member_payment'),
]