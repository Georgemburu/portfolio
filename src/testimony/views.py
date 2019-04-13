from django.shortcuts import render,get_list_or_404

from .models import Testimony 

# Create your views here.
def testimonyPageView(request,*args,**kwargs):
    testimonies = get_list_or_404(Testimony)

    context =  {
        "testimonies": testimonies,
        "heading":"Testimonies"
    }
    return render(request,'testimony/index.html',context)