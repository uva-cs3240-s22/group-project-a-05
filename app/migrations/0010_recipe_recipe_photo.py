# Generated by Django 4.0.3 on 2022-04-07 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_merge_20220406_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_photo',
            field=models.ImageField(default='defalut.jpg', upload_to='recipe_picture'),
        ),
    ]