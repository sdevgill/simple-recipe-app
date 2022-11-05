from django.contrib import admin

from .models import Recipe, Nutritionist, Client, Ingredient

admin.site.register(Nutritionist)
admin.site.register(Client)
admin.site.register(Recipe)
admin.site.register(Ingredient)