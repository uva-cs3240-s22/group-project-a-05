# Generated by Django 4.0.3 on 2022-04-06 22:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_alter_recipe_author_alter_recipe_user_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='user_forks',
            field=models.ManyToManyField(related_name='forked_recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]