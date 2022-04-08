from email.policy import default
from django.db import models
from django.contrib.auth import models as authmodels
# Create your models here.

class Recipe (models.Model):
    name        = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField(max_length=1000)
    time        = models.CharField(max_length=400)
    steps       = models.CharField(max_length=2000)
    image       = models.FileField(upload_to='recipe_picture/', null=True)

    author      = models.ForeignKey(authmodels.User, on_delete=models.CASCADE, related_name="posted_recipes")
    user_likes  = models.ManyToManyField(authmodels.User, related_name="liked_recipes")
    user_forks = models.ManyToManyField(authmodels.User, related_name="forked_recipes")

    forked_from_id = models.IntegerField(blank=True, null=True)
    forked_from_name= models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name

