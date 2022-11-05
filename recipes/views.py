from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)

from .models import Recipe


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

    def test_func(self):
        return self.get_object().user_can_view(self.request.user)