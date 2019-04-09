from enum import Enum

from django.db.models import Model as m
from django.db import models


class User(m):
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class FridgeDish(m):
    weight = models.IntegerField()


class FridgeIngredient(m):
    weight = models.IntegerField()


class UserIngredient(m):
    rate = models.IntegerField()


class UserCategory(m):
    category = models.IntegerField()


class UserMealPlan(m):
    meal = models.IntegerField()
    order_number = models.IntegerField()


class Goal(m):
    meal = models.IntegerField()
    description = models.CharField(max_length=20)


class GoalMealPlan(m):
    meal = models.IntegerField()
    order_number = models.IntegerField()


class GoalUsefulEnergy(m):
    callories = models.IntegerField()
    proteins = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()


class Dish(m):
    name = models.CharField(max_length=20)
    image_url = models.CharField(max_length=20)
    description = models.CharField(max_length=20)


class DishUsefulEnergy(m):
    callories = models.IntegerField()
    proteins = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()


class DishIngredient(m):
    pass


class Ingredient(m):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    image_url = models.CharField(max_length=20)


class IngredientUsefulEnergy(m):
    callories = models.IntegerField()
    proteins = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()


class Meal(m):
    pass


class Category(m):
    pass
