from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes=Recipe.objects.all()
    context={
        "Recipes" : recipes
    }
    return render(request, 'app/recipe_list.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if 'like' in request.POST:
        request.user.liked_recipes.add(recipe)
    elif 'unlike' in request.POST:
        request.user.liked_recipes.remove(recipe)
    
    return render(request, 'app/detail.html', { 'recipe' : recipe })

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

def profile(request):
    return render(request, 'app/userprofile.html')
