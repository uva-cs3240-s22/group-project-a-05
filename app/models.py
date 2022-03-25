from django.db import models
from django.contrib.auth import models as authmodels
# Create your models here.

class Recipe (models.Model):
    name        = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    ingredient  = models.CharField(max_length=1000)
    time        = models.CharField(max_length=400)
    step        = models.CharField(max_length=2000)

    user_like   = models.ManyToManyField(authmodels.User, related_name= "like_recipe")

    def __str__(self):
        return self.name
    

