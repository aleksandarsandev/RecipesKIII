# Generated by Django 5.0.3 on 2024-09-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('list_of_ingredients', models.CharField(max_length=250)),
                ('minutes_to_prepare', models.IntegerField()),
                ('description_of_preparation', models.CharField(max_length=250)),
            ],
        ),
    ]
