from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    list_of_ingredients = models.CharField(max_length=250)
    minutes_to_prepare = models.IntegerField()
    description_of_preparation = models.CharField(max_length=250)

    def __str__(self):
        return self.name
