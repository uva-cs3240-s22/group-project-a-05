from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def create_recipe(request):
    return render(request, 'app/create_recipe.html')

def userprofile(request):
    print(request.user.like_recipe.all())
    return render(request, 'app/userprofile.html')