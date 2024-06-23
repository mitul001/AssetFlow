from django.db import models

# Create your models here.
class Contact(models.Model):

    CONTACT_TYPE_CHOICES = [
        ('seller','Seller'),
        ('buyer','Buyer'),
        ('both','Both')
    ]

    name = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=10, choices=CONTACT_TYPE_CHOICES,default='both')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(null=True)
    tax_id = models.CharField(max_length=20)
    website = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

  