from django.db import models

# Create your models here.
class Connect(models.Model):
    title = models.CharField(max_length=100)
    icon_url = models.CharField(max_length=150)
    url = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.title}'