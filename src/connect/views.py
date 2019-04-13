from django.shortcuts import render,get_list_or_404
from .models import Connect
# Create your views here.
def connectPageView(request,*args,**kwargs):
    conn = get_list_or_404(Connect)
    context = {
        "conn": conn,
        "heading":"Connect"
    }
    return render(request,'connect/index.html',context)