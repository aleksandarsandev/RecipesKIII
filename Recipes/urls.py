"""
URL configuration for Recipes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RecipesApp import views
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipes_list, name='recipes_list'),
    path('recipe/details/<str:pk>/', views.recipe_detail, name='recipe_detail'),  # Changed <int:pk> to <str:pk>
    path('recipe/new/', views.recipe_add, name='recipe_add'),
    path('recipe/<str:pk>/edit/', views.recipe_edit, name='recipe_edit'),  # Changed <int:pk> to <str:pk>
    path('recipe/<str:pk>/delete/', views.recipe_delete, name='recipe_delete'),  # Changed <int:pk> to <str:pk>
    path('delete-all-recipes/', views.delete_all_recipes, name='delete_all_recipes'),
    ]
