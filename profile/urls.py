from django.urls import re_path

import profile.views as views

urlpatterns = [

    re_path(r'info', views.CurrentProfile.as_view()),
    re_path(r'goal', views.CurrentUserGoal.as_view()),
    re_path(r'categories', views.CurrentUserCategory.as_view()),
    re_path(r'ingredients', views.CurrentUserIngredient.as_view()),
]
