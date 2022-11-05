from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Nutritionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    nutritionist = models.ForeignKey(Nutritionist, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')
    # ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
    portions = models.IntegerField(default=1)
    nutritionist = models.ForeignKey(Nutritionist, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def user_can_view(self, user):
        return self.user == user or self.nutritionist.user == user

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})
