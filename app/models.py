from email.policy import default
from django.db import models
from django.contrib.auth import models as authmodels
# Create your models here.

class Recipe (models.Model):
    name        = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    time        = models.CharField(max_length=400)
    image       = models.FileField(upload_to='recipe_picture/')

    author      = models.ForeignKey(authmodels.User, on_delete=models.CASCADE, related_name="posted_recipes")
    forked_from = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name="child_recipes")
    user_likes  = models.ManyToManyField(authmodels.User, related_name="liked_recipes")

    def __str__(self):
        return self.name


class Ingredient (models.Model):
    recipe  = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name    = models.CharField(max_length=400)
    amount  = models.FloatField()
    units   = models.CharField(max_length=50) #larger than necessary, change later

    class Meta:
        order_with_respect_to = 'recipe'

    def __str__(self):
        return self.name


class Step (models.Model):
    recipe  = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps_list')
    text    = models.CharField(max_length=500)

    class Meta:
        order_with_respect_to = 'recipe'
    
    def __str__(self):
        return self.text

class Comment(models.Model):
    author          = models.ForeignKey(authmodels.User, on_delete=models.CASCADE, related_name="comments")
    recipe          = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    comment_text    = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment_text
