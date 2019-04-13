from django.db import models
from framework.models import Framework
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField()
    live_url = models.URLField()
    framework = models.ForeignKey(Framework,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return f'{self.framework} project {self.title }'

class ProjectImage(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to="project_pics",null=True)
    project = models.ForeignKey(Project,on_delete=models.PROTECT)


    def __str__(self):
        return f'project {self.title } image'