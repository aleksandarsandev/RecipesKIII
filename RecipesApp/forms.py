from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'list_of_ingredients', 'minutes_to_prepare', 'description_of_preparation']