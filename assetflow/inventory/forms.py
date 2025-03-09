from django import forms
from .models import InventoryTransaction

class InventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        exclude = ['total_price','price']
