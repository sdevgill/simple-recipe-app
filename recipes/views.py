from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
)

from .models import Recipe, Nutritionist, Client, Ingredient


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"


class RecipeDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    def test_func(self):
        return self.get_object().user_can_view(self.request.user)