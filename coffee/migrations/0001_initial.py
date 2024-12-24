# Generated by Django 4.2.17 on 2024-12-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=254)),
                ('country_of_origin', models.CharField(max_length=254)),
                ('year_of_harvest', models.CharField(max_length=254)),
                ('variety', models.CharField(max_length=254)),
                ('colour', models.CharField(max_length=254)),
                ('processing_method', models.CharField(max_length=254)),
                ('aroma', models.DecimalField(decimal_places=2, max_digits=4)),
                ('flavour', models.DecimalField(decimal_places=2, max_digits=4)),
                ('aftertaste', models.DecimalField(decimal_places=2, max_digits=4)),
                ('acidity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('body', models.DecimalField(decimal_places=2, max_digits=4)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=4)),
                ('unifirmity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('sweetness', models.DecimalField(decimal_places=2, max_digits=4)),
                ('moisture', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Coffee Quality',
            },
        ),
    ]