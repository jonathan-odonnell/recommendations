# Generated by Django 4.2.17 on 2024-12-29 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_nutrient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat',
            old_name='cholestorol',
            new_name='cholesterol',
        ),
        migrations.RenameField(
            model_name='stat',
            old_name='vitimin_a',
            new_name='vitamin_a',
        ),
        migrations.RenameField(
            model_name='stat',
            old_name='vitimin_c',
            new_name='vitamin_c',
        ),
    ]
