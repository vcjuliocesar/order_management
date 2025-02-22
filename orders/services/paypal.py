from orders.domain.contracts.payment_interface import PaymentMethod


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount} USD"
