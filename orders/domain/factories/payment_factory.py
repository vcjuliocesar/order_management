from orders.services.credit_card import CreditCardPayment
from orders.services.paypal import PayPalPayment

class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        payment_methods = {
            "credit_card":CreditCardPayment(),
            "paypal":PayPalPayment(),
        }
        return payment_methods.get(method,None)