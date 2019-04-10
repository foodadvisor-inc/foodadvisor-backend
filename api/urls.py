from django.urls import re_path
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    re_path(r'^login/', authtoken_views.obtain_auth_token),
]
