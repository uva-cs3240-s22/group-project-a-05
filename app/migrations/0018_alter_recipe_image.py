# Generated by Django 4.0.3 on 2022-04-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_merge_20220408_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.FileField(null=True, upload_to='recipe_picture/'),
        ),
    ]