# Generated by Django 4.0.3 on 2022-03-26 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_recipe_user_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='user_like',
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_recipes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user_likes',
            field=models.ManyToManyField(related_name='liked_recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
