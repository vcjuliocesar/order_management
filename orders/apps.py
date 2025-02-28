from django.apps import AppConfig
from django.db.utils import OperationalError
from django.core.exceptions import ObjectDoesNotExist

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):

        from .models import Order
        from decimal import Decimal

        try:

            if not Order.objects.exists():

                Order.objects.create(total_amount=Decimal('150.00'), payment_method="credit_card")
                Order.objects.create(total_amount=Decimal('200.00'), payment_method="paypal")

                #print("Datos de prueba insertados en la tabla orders")
                # esto es una prueba
        
        except (OperationalError, ObjectDoesNotExist):
            pass