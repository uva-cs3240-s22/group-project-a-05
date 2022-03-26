from django.shortcuts import render
from .models import Recipe

# Create your views here.
def index(request):
    return render(request, 'app/index.html', { 'recipes': Recipe.objects.all() })

def create_recipe(request):
    try:
        recipename=request.POST.get("recipe_name")
        recipetime=request.POST.get("recipe_time")
        recipedescription=request.POST.get("recipe_description")
        recipeingredients=request.POST.get("recipe_ingredients")
        recipesteps=request.POST.get("recipe_steps")
    except (KeyError):
        return render(request, 'app/create_recipe.html', {
            'error_message': "You didn't enter a recipe",
        })
    else:
        if recipename==None and recipetime==None and recipedescription==None and recipeingredients==None and recipesteps==None:
            return render(request, 'app/create_recipe.html', {
            'error_message': "You didn't enter a recipe",
        })
        recipes=Recipe(name=recipename, description=recipedescription, ingredients=recipeingredients, time=recipetime, steps=recipesteps)
        recipes.save()
    return render(request, 'app/create_recipe.html' )

def recipe_list(request):
    recipes=Recipe.objects.all()
    context={
        "Recipes" : recipes
    }
    return render(request, 'app/recipe_list.html', context)

def profile(request):
    return render(request, 'app/userprofile.html')
