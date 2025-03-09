from django.shortcuts import render, get_object_or_404, redirect
from .models import InventoryTransaction
from .forms import InventoryForm

# List all transactions
def inventory_list_view(request):
    transactions = InventoryTransaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'inventory_list.html', context)

# Create a transaction (Buy/Sell)
def inventory_create_view(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            selected_product = form.cleaned_data.get('products')
            quantity = form.cleaned_data.get('quantity')

            if selected_product and quantity:
                transaction.price = selected_product.price
                transaction.total_price = selected_product.price * quantity  
            transaction.save()
            return redirect('list_inventory')
    form = InventoryForm()
    context ={
        'forms':form,
    }
    return render(request,'inventory_form.html',context)

# Create or update a transaction (Buy/Sell)
def inventory_create_update_view(request, id=None):
    transaction = get_object_or_404(InventoryTransaction, id=id)

    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save(commit=False)
            selected_product = form.cleaned_data.get('products')
            quantity = form.cleaned_data.get('quantity')

            if selected_product and quantity:
                transaction.price = selected_product.price
                transaction.total_price = selected_product.price * quantity
            transaction.save()
            return redirect('list_inventory')
    else:
        form = InventoryForm(instance=transaction)
    context = {'forms': form, 'transaction': transaction}
    return render(request, 'inventory_form.html', context)

# Delete a transaction
def inventory_delete_view(request, id):
    transaction = get_object_or_404(InventoryTransaction, id=id)
    transaction.delete()
    return redirect('list_inventory')
