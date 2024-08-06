from django.contrib import admin
from django.urls import path, include
from recipe.views import *

urlpatterns = [
    path('', recipes, name = "recipes"),
    path('delete-recipe/<id>/', delete_recipe, name = "delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name = "update_recipe"),
]
