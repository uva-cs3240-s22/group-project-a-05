from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('',                            views.recipe_list,      name='index'), 
    path('create',                      views.create_recipe,    name='create_recipe'),
    path('submit',                      views.submit_recipe,    name='submit_recipe'),
    path('profile',                     views.profile,          name='profile'),
    path('detail/<int:recipe_id>',      views.detail,           name='detail'),
    path('like/<int:recipe_id>',        views.like,             name='like'),
    path('unlike/<int:recipe_id>',      views.unlike,           name='unlike'),
    path('fork/<int:recipe_id>',        views.fork,             name='fork'),
    path('submit_fork/<int:recipe_id>', views.submit_fork,      name='submit_fork'),
]