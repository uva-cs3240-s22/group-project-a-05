# Generated by Django 4.0.3 on 2022-04-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_recipe_user_forks'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='forked_from',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]