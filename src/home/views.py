from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.generic import (
    ListView,
)

from .models import Skill
from portfolio.tags import getTags
# Create your views here.

# def homePageView(request,*args,**kwargs):
#     skills = Skill.objects.all()
#     # skills = get_object_or_404(Skill)

#     context = {
#         "skills": skills,
#         "title": "Home",
#         "heading":"Skills"
#     }
#     return render(request,'home/index.html',context)

class homePageView(ListView):
    model = Skill
    template_name = 'home/index.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'skills'
    
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = {}
        # context = super().get_context_data(**kwargs)
        context["skills"] = get_list_or_404(Skill)
        context["heading"] = "Skills"
        context["url"] = '/skill/'
        context["urls_tags"] = getTags(0)
        return context
        
    

