from django.db import models

from category.models import Category
from language.models import Language

# Create your models here.
class Framework(models.Model):
    
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='framework_pics')
    # slug = models.SlugField(max_length=100)
    language = models.CharField(max_length=100)


    category = models.ForeignKey(Category,on_delete=models.PROTECT)


    def __str__(self):
        return f'{self.language} {self.title}'