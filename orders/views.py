from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.domain.factories.payment_factory import PaymentFactory
from .serializers import OderSerializer
from .models import Order

# Create your views here.

@api_view(["POST"])
def post_order(self,order_id):
    try:
        order = Order.objects.get(id=order_id)
        payment_method = PaymentFactory.get_payment_method(order.payment_method)

        if not payment_method:
            return Response({"error": "Invalid payment method"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment_response = payment_method.process_payment(order.total_amount)
        return Response({"message": payment_response}, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
