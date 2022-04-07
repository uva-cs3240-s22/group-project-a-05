from django.db import models
from django.contrib.auth import models as authmodels
# Create your models here.

class Recipe (models.Model):
    name        = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField(max_length=1000)
    time        = models.CharField(max_length=400)
    steps       = models.CharField(max_length=2000)

    author      = models.ForeignKey(authmodels.User, on_delete=models.CASCADE, related_name="posted_recipes")
    user_likes  = models.ManyToManyField(authmodels.User, related_name="liked_recipes")
    user_forks = models.ManyToManyField(authmodels.User, related_name="forked_recipes")

    def __str__(self):
        return self.name

