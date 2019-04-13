from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def contactPageView(request,*args,**kwargs):
    form = ContactForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            form = ContactForm()
            
    context = {
        "heading": "Contact",
        "form": form,
    }
    return render(request,'contact/index.html',context)