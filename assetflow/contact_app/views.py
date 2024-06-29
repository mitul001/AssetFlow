from django.shortcuts import render,redirect
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
    context={
        'contact':item_list,
    }
    return render(request,'list.html',context)