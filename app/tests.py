from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe
from django.urls import reverse

# Create your tests here.
class DummyTest(TestCase):
    def testShouldWork(self):
        self.assertTrue(True)

class recipeTest(TestCase):
    def create_recipe(self, name="Chicken", description="Roasted Chicken", ing="Chicken, Garlic", time="30 minutes", steps="1. Roast Chicken 2. Enjoy"):
        test_user = User.objects.create(username='test user')
        return Recipe.objects.create(name=name, description=description, ingredients=ing, time=time, steps=steps, author=test_user)

    def test_create_recipe(self):
        rep=self.create_recipe()
        self.assertTrue(isinstance(rep, Recipe))
        self.assertEqual("Chicken", rep.name)
        self.assertEqual("Roasted Chicken", rep.description)
        self.assertEqual("Chicken, Garlic", rep.ingredients)
        self.assertEqual("30 minutes", rep.time)
        self.assertEqual("1. Roast Chicken 2. Enjoy", rep.steps)

    def test_create_recipe_view(self):
        resp = self.client.get('/create')
        self.assertEqual(resp.status_code, 200)

    def test_recipes_list_view(self):
        resp=self.client.get('')
        self.assertEqual(resp.status_code, 200)
