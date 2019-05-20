from django.contrib import admin

from api.models import *

Models = (Profile, UserCategory, UserIngredient, UserMealPlan, UserUsefulEnergy,
          IngredientUsefulEnergy, Ingredient, GoalMealPlan, Goal, FridgeIngredient,
          DishIngredient, Dish)

admin.site.register(Models)
