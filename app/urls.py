from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'), 
    path('create', views.create_recipe, name="create_recipe"),
    path('recipes', views.recipe_list, name='recipe_list'),
    path('profile', views.profile, name="profile"),
]