from django.urls import path
from .views import post_order

urlpatterns = [
    path('order/<int:order_id>/pay/',post_order,name='process-payment'),
]