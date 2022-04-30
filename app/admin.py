from django.contrib import admin
from .models import Recipe, Ingredient, Step

class IngredientInline (admin.TabularInline):
    model = Ingredient
    extra = 0

class StepInline (admin.TabularInline):
    model = Step
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, StepInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["user_likes"].required = False
        form.base_fields["forked_from"].required = False
        form.base_fields["image"].required = False
        return form

admin.site.register(Recipe, RecipeAdmin)