from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.generic import (
    ListView,
)
from .models import Framework
from category.models import Category
from portfolio.tags import getTags
# Create your views here

# def frameworkPageView(request,*args,**kwargs):
#     frmwrk = Framework.Objects.all().filter(language = kwargs[0])
#     print(frmwrk)
#     context = {

#     }
#     return render(request,'framework/listing.html',context)


class frameworkPageView(ListView):
    model = Framework
    template_name = 'framework/listing.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'skills'
    
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = {}
        context["heading"] = f'**{self.kwargs["slug"]}**'
        context["skills"] = get_list_or_404(Framework, language=self.kwargs["slug"])
        context["urls_tags"] = getTags(1)
        return context