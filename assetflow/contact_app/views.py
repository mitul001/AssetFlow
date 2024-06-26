from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_create_view(request):
    if request.method == 'POST':
        form = ContactForm(request.post)
        if form.is_valid():
            form.save()
            return render(request,'contact.html')
    form = ContactForm()
    context ={
        'forms':form,
    }
    return render(request,'contact.html',context)

def contact_list_view(request):
    item_list = Contact.objects.all()
    print(item_list)
    context={
        'contact':item_list,
    }
    return render(request,'list.html',context)