from django.db import models

# Create your models here.

class recipe (models.Model):
    name=models.CharField(max_length=400)
    description=models.TextField(null=True)
    ingredients=models.TextField(null=True)
    time=models.CharField(max_length=400)
    steps=models.TextField(null=True)
    def _str_(self):
        return self.name
