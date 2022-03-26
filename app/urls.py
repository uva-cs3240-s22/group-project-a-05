from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'), 
    path('create', views.create_recipe, name="create_recipe"),
    path('profile', views.profile, name="profile")
]