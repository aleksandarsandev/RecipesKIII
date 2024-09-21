from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
from bson import ObjectId
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm  # Make sure you have a form for your recipe model
# Create your views here.


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes': recipes})
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)  # Don't save yet
            recipe.save()  # Save after setting the ObjectId
            return redirect('recipes_list')  # Use pk as a string
    else:
        form = RecipeForm()
    return render(request, 'recipe_add.html', {'form': form})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)  # Here pk is a string
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, id=ObjectId(pk))  # Use ObjectId for MongoDB
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=str(recipe.id))  # Use str for ObjectId
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_edit.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, id=ObjectId(pk))  # Use ObjectId for MongoDB
    if request.method == "POST":
        recipe.delete()
        return redirect('recipes_list')
    return render(request, 'recipe_delete.html', {'recipe': recipe})

def delete_all_recipes(request):
    if request.method == "POST":
        Recipe.objects.all().delete()  # Delete all Recipe objects
        return redirect('recipes_list')  # Redirect to the recipes list page

    return render(request, 'confirm_delete_all.html')