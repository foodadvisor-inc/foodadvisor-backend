from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _

GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_NOT_SPECIFIED = 2

GENDER_CHOICES = (
    (GENDER_MALE, _('male')),
    (GENDER_FEMALE, _('female')),
    (GENDER_NOT_SPECIFIED, _('not specified')),
)

MEAL_FIRST_COURSE = 0
MEAL_MAIN_COURSE = 1
MEAL_LUNCH = 2
MEAL_SNACK = 3
MEAL_SALAD = 4
MEAL_DESSERT = 5

MEAL_CHOICES = (
    (MEAL_FIRST_COURSE, "first course"),
    (MEAL_MAIN_COURSE, "main course"),
    (MEAL_LUNCH, "lunch"),
    (MEAL_SNACK, "snack"),
    (MEAL_SALAD, "salad"),
    (MEAL_DESSERT, "dessert"),
)

CATEGORY_MEAT = 0
CATEGORY_MILK = 1
CATEGORY_FISH = 2
CATEGORY_SHELLFISH = 3
CATEGORY_SUGAR = 4
CATEGORY_FRUCTOSE = 5
CATEGORY_GLUTEN = 6
CATEGORY_PEANUT = 7
CATEGORY_SOY = 8
CATEGORY_EGG = 9
CATEGORY_NUT = 10

CATEGORY_CHOICES = (
    (CATEGORY_MEAT, "meat"),
    (CATEGORY_MILK, "milk"),
    (CATEGORY_FISH, "fish"),
    (CATEGORY_SHELLFISH, "shellfish"),
    (CATEGORY_SUGAR, "sugar"),
    (CATEGORY_FRUCTOSE, "fructose"),
    (CATEGORY_GLUTEN, "gluten"),
    (CATEGORY_PEANUT, "peanut"),
    (CATEGORY_SOY, "soy"),
    (CATEGORY_EGG, "egg"),
    (CATEGORY_NUT, "tree nut"),
)


class Goal(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, null=True, on_delete=models.SET_NULL)

    birth_date = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=GENDER_NOT_SPECIFIED,
                                              blank=False, null=False)
    height = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(300)])
    weight = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(500000)])


class GoalMealPlan(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    meal = models.PositiveSmallIntegerField(choices=MEAL_CHOICES, default=MEAL_FIRST_COURSE,
                                            blank=False, null=False)
    order_number = models.IntegerField()


class GoalUsefulEnergy(models.Model):
    goal = models.OneToOneField(Goal, on_delete=models.CASCADE, primary_key=True)

    calories = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    proteins = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    fat = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    carbohydrates = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])


class Dish(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.CharField(max_length=300)
    description = models.CharField(max_length=300)


class DishUsefulEnergy(models.Model):
    dish = models.OneToOneField(Dish, on_delete=models.CASCADE, primary_key=True)

    calories = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    proteins = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    fat = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    carbohydrates = models.PositiveSmallIntegerField(blank=True, null=True, default=0,
                                                     validators=[MaxValueValidator(100000)])


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, default=CATEGORY_MEAT,
                                                blank=False, null=False)
    image_url = models.CharField(max_length=300)


class IngredientUsefulEnergy(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, primary_key=True)

    calories = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    proteins = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    fat = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])
    carbohydrates = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(100000)])


class DishIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


class FridgeDish(models.Model):
    fridge = models.ForeignKey(Profile, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    weight = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(500000)])


class FridgeIngredient(models.Model):
    fridge = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    weight = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(500000)])


class UserIngredient(models.Model):
    preferences = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    rate = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(500000)])


class UserCategory(models.Model):
    preferences = models.ForeignKey(Profile, on_delete=models.CASCADE)

    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, default=CATEGORY_MEAT,
                                                blank=False, null=False)


class UserMealPlan(models.Model):
    preferences = models.ForeignKey(Profile, on_delete=models.CASCADE)

    meal = models.PositiveSmallIntegerField(choices=MEAL_CHOICES, default=MEAL_FIRST_COURSE,
                                            blank=False, null=False)
    order_number = models.IntegerField(blank=True, null=True)
