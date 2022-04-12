from email.policy import default
from django.db import models
from django.contrib.auth import models as authmodels
# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(authmodels.User, on_delete=models.CASCADE, related_name="comments")
    comment_text=models.CharField(max_length=1000)

    def __str__(self):
        return self.comment_text
class Recipe (models.Model):
    name        = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField(max_length=1000)
    time        = models.CharField(max_length=400)
    steps       = models.CharField(max_length=2000)
    image       = models.FileField(upload_to='recipe_picture/', null=True)

    author      = models.ForeignKey(authmodels.User, on_delete=models.CASCADE, related_name="posted_recipes")
    forked_from = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name="child_recipes")
    user_likes  = models.ManyToManyField(authmodels.User, related_name="liked_recipes")

    comments=models.ManyToManyField(Comment, blank=True, related_name="recipe_comments" )

    def __str__(self):
        return self.name
