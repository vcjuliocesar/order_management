from orders.domain.contracts.payment_interface import PaymentMethod


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount} USD"
