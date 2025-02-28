from django.db import models

# Create your models here.
class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id} - {self.total_amount} USD"