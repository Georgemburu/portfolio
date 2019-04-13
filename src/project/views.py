from django.shortcuts import render,get_list_or_404
from .models import Project,ProjectImage
from django.views.generic import (
    ListView,
)
from portfolio.tags import getTags

# Create your views here.

def projectViewPage(request,*args,**kwargs):
    
    slug_skill = kwargs["slug"]
    slug_framework = kwargs["string"]

    projs = get_list_or_404(Project)
    projimgs = ProjectImage.objects.all()
    

    projlist = []
    projimglist = []
    

    for p in projs:
        if p.framework.title == slug_framework and p.framework.language == slug_skill:
            projlist.append(p)
        

    for i in projimgs:
        projimglist.append(i)
    
    projperimgs = []
    for p in projlist:
        imgsr = []
        for r in projimglist:
            if p == r.project:
                imgsr.append(r)
        
        group = {
            "image":imgsr,
            "project":p
        }
        projperimgs.append(group)

               
                
                


    # group = {"image":p,"project":r  }

    context = {
        "obj": projperimgs,
        "heading": "***Projects***",
        "urls_tags": getTags(2)

    }
    return render(request,'project/project_list.html',context)

# class projectViewPage(ListView):
#     model = Project
#     pics = get_list_or_404(ProjectImage, project = )
#     # template_name = 'project/project_list.html'  # <app>/<model>_<viewtype>.html
#     # context_object_name = 'skills'/home/george/Desktop/portfolio/src/project/template/
#     context_object_name = "skills"
#     paginate_by = 2

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context["skills"] = Project.Objects.all()
#         context["heading"] = "Pojects"
        
#         return context
        
    