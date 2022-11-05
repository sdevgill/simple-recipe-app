from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, Nutritionist, Client, Ingredients


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
