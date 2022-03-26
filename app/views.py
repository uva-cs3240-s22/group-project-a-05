from django.shortcuts import render
from .models import Recipe

# Create your views here.
def index(request):
    return render(request, 'app/index.html', { 'recipes': Recipe.objects.all() })

def create_recipe(request):
    return render(request, 'app/create_recipe.html')

def profile(request):
    return render(request, 'app/userprofile.html')