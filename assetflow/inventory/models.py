from django.db import models

# Create your models here.
from django.db import models
from contact_app.models import Contact
from product_app.models import Product

class InventoryTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.contact.name} on {self.transaction_date.strftime('%Y-%m-%d')}"
 