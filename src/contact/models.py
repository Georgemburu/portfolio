from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150, null=True)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return f'by {self.name}'
