from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.contrib.auth.models import User
from rest_auth.registration.views import SocialLoginView
from rest_framework import viewsets, generics
from .serializers import Goal, GoalSerializer

from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for USERS
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class GoalList(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer