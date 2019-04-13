from django.db import models

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='skills_dp')


    def __str__(self):
        return f'{self.title}_skill'