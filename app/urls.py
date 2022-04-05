from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.recipe_list, name='index'), 
    path('create', views.create_recipe, name='create_recipe'),
    path('profile', views.profile, name='profile'),
    path('detail/<int:recipe_id>', views.detail, name='detail'),
    path('fork/<int:recipe_id>',views.fork,name='fork')
]