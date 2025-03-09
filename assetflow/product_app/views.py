from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'product_list.html', context)

def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    form = ProductForm()
    context ={
        'forms':form,
    }
    return render(request,'product_form.html',context)

def product_create_update_view(request,id=None):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    else:
        form = ProductForm(instance=product)
    context = {'forms': form, 'product': product}

    return render(request, 'product_form.html', context)

# Delete a product
def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('list_product')
