from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_create_view(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contact')
    form = ContactForm()
    context ={
        'forms':form,
    }
    return render(request,'contact.html',context)

def contact_list_view(request):
    item_list = Contact.objects.all()
    # breakpoint()
    context={
        'contact':item_list,
    }
    return render(request,'list.html',context)

def update_contact_view(request,id):
    contact = get_object_or_404(Contact,id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list_contact')
    else:
        form = ContactForm(instance=contact)
    context ={
        'forms':form,
        'contact':contact,
    }
    return render(request, 'contact.html', context)

def delete_contact_view(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('list_contact') 