from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
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
    return render(request, 'app/create_recipe.html' )

def submit_recipe(request):
    if request.user.is_authenticated:
        try:
            recipename = request.POST.get("recipe_name")
            recipetime = request.POST.get("recipe_time")
            recipedescription = request.POST.get("recipe_description")
            recipeingredients = request.POST.get("recipe_ingredients")
            recipesteps = request.POST.get("recipe_steps")
            recipeimage=request.FILES.get("recipe_image")
            #print(request.POST)
            #print(request.FILES)
        except (KeyError):
            return HttpResponseRedirect(reverse('app:create_recipe'))
        else:
            if not(recipename and recipetime and recipedescription and recipeingredients and recipesteps and recipeimage):
                return HttpResponseRedirect(reverse('app:create_recipe'))
            recipes=Recipe(author=request.user, name=recipename, description=recipedescription, ingredients=recipeingredients, time=recipetime, steps=recipesteps, image=recipeimage)
            recipes.save()

            return HttpResponseRedirect(reverse('app:profile'))
    else:
        return HttpResponseRedirect(reverse('app:create_recipe'))

def profile(request):
    return render(request, 'app/userprofile.html')

def fork(request,recipe_id):
    recipe=Recipe.objects.get(pk=recipe_id)
    return render(request,'app/fork_recipe.html',{'recipe':recipe})