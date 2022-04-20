from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Recipe, Comment
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
        client = Client()
        res=client.get('/create')
        self.assertTemplateUsed(res, "app/create_recipe.html")

    def test_recipes_list_view(self):
        client = Client()
        res=client.get('/')
        self.assertTemplateUsed(res, "app/recipe_list.html")

    def test_detail_view(self):
        client = Client()
        rep=self.create_recipe()
        res=client.get('/detail/1')
        self.assertTemplateUsed(res, "app/detail.html")

    def test_user_profile_view(self):
        client=Client()
        test_user = User.objects.create(username='test user')
        rep=Recipe.objects.create(name="Chick", description="des", ingredients="ing",time="1", steps="steps", author=test_user)
        client.force_login(test_user)
        res=client.get('/profile')
        self.assertTemplateUsed(res, "app/userprofile.html")

    def test_fork_view(self):
        client=Client()
        rep=self.create_recipe()
        res=client.get("/fork/1")
        self.assertTemplateUsed(res, "app/fork_recipe.html")

    def test_comment_view(self):
        client = Client()
        rep=self.create_recipe()
        res=client.get("/comment/1")
        self.assertTemplateUsed("app/create_comment.html")

    def test_rep_in_user_likes(self):
        client=Client()
        req=client.get(reverse('app:index'))
        req.test_user = User.objects.create(username='test user')
        rep= Recipe.objects.create(name="Chick", description="des", ingredients="ing",time="1", steps="steps", author=req.test_user)
        client.force_login(req.test_user)
        rep.author.liked_recipes.add(rep)
        res=client.get("/profile")
        self.assertContains(res, rep)

    def test_rep_in_posted_rep(self):
        client=Client()
        req=client.get(reverse('app:index'))
        req.test_user = User.objects.create(username='test user')
        rep= Recipe.objects.create(name="Chick", description="des", ingredients="ing",time="1", steps="steps", author=req.test_user)
        client.force_login(req.test_user)
        res=client.get("/profile")
        self.assertContains(res, rep)

    def test_create_comment(self):
        client=Client()
        req=client.get(reverse('app:index'))
        req.test_user = User.objects.create(username='test user')
        rep= Recipe.objects.create(name="Chick", description="des", ingredients="ing",time="1", steps="steps", author=req.test_user)
        client.force_login(req.test_user)
        com=Comment.objects.create(author=req.test_user, comment_text="Hi", recipe=rep)
        self.assertEquals("Hi", com.comment_text)
        self.assertEquals(req.test_user, com.author)
        self.assertEquals(rep, com.recipe)

    def test_comment_posted(self):
        client=Client()
        req=client.get(reverse('app:index'))
        req.test_user = User.objects.create(username='test user')
        rep= Recipe.objects.create(name="Chick", description="des", ingredients="ing",time="1", steps="steps", author=req.test_user)
        client.force_login(req.test_user)
        com=Comment.objects.create(author=req.test_user, comment_text="Hi", recipe=rep)
        res=client.get("/detail/1")
        self.assertContains(res, com)

    def test_unlike(self):
        client=Client()
        req=client.get(reverse('app:index'))
        req.test_user = User.objects.create(username='test user')
        req.test_user2 = User.objects.create(username='test user two')
        rep= Recipe.objects.create(name="Chick", description="des", ingredients="ing",time="1", steps="steps", author=req.test_user)
        rep2=Recipe.objects.create(name="Meat", description="des", ingredients="ing",time="1", steps="steps", author=req.test_user2)
        client.force_login(req.test_user)
        rep.author.liked_recipes.add(rep2)
        res=client.get("/profile")
        self.assertContains(res, rep2)
        rep.author.liked_recipes.remove(rep2)
        res=client.get("/profile")
        self.assertNotContains(res, rep2)

    def test_delete_comment(self):
        client=Client()
        req=client.get(reverse('app:index'))
        req.test_user = User.objects.create(username='test user')
        rep= Recipe.objects.create(name="Chick", description="des", ingredients="ing",time="1", steps="steps", author=req.test_user)
        client.force_login(req.test_user)
        com=Comment.objects.create(author=req.test_user, comment_text="Hi", recipe=rep)
        res=client.get("/detail/1")
        self.assertContains(res, com)
        com.delete()
        res=client.get("/profile")
        self.assertNotContains(res, com)

    def test_search_view(self):
        client=Client()
        res=client.get('/searchbar')
        self.assertTemplateUsed("app/searchbar.html")

    


    
