from django.db import models

# Create your models here.

class recipe (models.Model):
    name=models.CharField(max_length=400)
    description=models.CharField(max_length=1000)
    ingredient=models.CharField(max_length=1000)
    time=models.CharField(max_length=400)
    step=models.CharField(max_length=2000)
    def _str_(self):
        return self.name
