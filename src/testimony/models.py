from django.db import models

# Create your models here.
class Testimony(models.Model):
    name = models.CharField(max_length=150)
    image = models.FileField(upload_to='testimony_pics')
    body = models.TextField()



    def __str__(self):
        return f'by {self.name}'
