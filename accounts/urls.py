from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('orders', views.order_history, name='order_history'),
]