from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Ingredient
from django.urls import reverse

# Create your tests here.
class DummyTest(TestCase):
    def testShouldWork(self):
        self.assertTrue(True)

class recipeTest(TestCase):
    def create_recipe(self, name="Chicken", description="Roasted Chicken", ing=[], time="30 minutes", steps="1. Roast Chicken 2. Enjoy"):
        test_user = User.objects.create(username='test user')
        recipe = Recipe.objects.create(name=name, description=description, time=time, steps=steps, author=test_user)
        for ingredient in ing:
            Ingredient.objects.create(recipe=recipe, name=ingredient['name'], amount=ingredient['amount'], units=ingredient['units'])
        return recipe

    def test_create_recipe(self):
        rep=self.create_recipe(ing=[{'name':'Chicken', 'amount':1, 'units':""}, {'name':'Garlic', 'amount':1, 'units':'some'}])
        self.assertTrue(isinstance(rep, Recipe))
        self.assertEqual("Chicken", rep.name)
        self.assertEqual("Roasted Chicken", rep.description)
        self.assertEqual("Chicken", rep.ingredients.all()[0].name)
        self.assertEqual(1, rep.ingredients.all()[0].amount)
        self.assertEqual("", rep.ingredients.all()[0].units)
        self.assertEqual("Garlic", rep.ingredients.all()[1].name)
        self.assertEqual(1, rep.ingredients.all()[1].amount)
        self.assertEqual("some", rep.ingredients.all()[1].units)
        self.assertEqual("30 minutes", rep.time)
        self.assertEqual("1. Roast Chicken 2. Enjoy", rep.steps)

    def test_create_recipe_view(self):
        resp = self.client.get('/create')
        self.assertEqual(resp.status_code, 200)

    def test_recipes_list_view(self):
        resp=self.client.get('')
        self.assertEqual(resp.status_code, 200)
