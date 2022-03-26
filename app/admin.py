from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["user_likes"].required = False
        return form

admin.site.register(Recipe, RecipeAdmin)