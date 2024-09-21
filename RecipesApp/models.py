from django.db import models
from bson import ObjectId

# Function to generate ObjectId
def generate_object_id():
    return str(ObjectId())

# Create your models here.
class Recipe(models.Model):
    id = models.CharField(max_length=24, primary_key=True, default=generate_object_id)  # No parentheses
    name = models.CharField(max_length=50)
    list_of_ingredients = models.CharField(max_length=250)
    minutes_to_prepare = models.IntegerField()
    description_of_preparation = models.CharField(max_length=250)

    def __str__(self):
        return self.name
