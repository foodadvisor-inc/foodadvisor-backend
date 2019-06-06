from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import viewsets

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for USERS
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Ingredients
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
