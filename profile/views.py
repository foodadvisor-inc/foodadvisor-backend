from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import IsAuthenticated

from api.serializers import *
from profile.schemas import CurrentUserCategorySchema, CurrentUserIngredientSchema, CurrentUserProfileSchema, \
    CurrentUserGoalSchema


def get_choice(display_value, choices):
    for item in choices:
        if item[1] == display_value:
            return item[0]
    return None


class CurrentProfile(views.APIView):

    schema = CurrentUserProfileSchema()

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Get user profile
        """

        profile = Profile.objects.get(user=request.user)
        return JsonResponse(ProfileSerializer(profile).data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        """
         Add profile info
        """
        profile = request.data
        profile['user'] = request.user.id
        serializer = ProfileSerializer(data=profile, partial=True)

        if (serializer.is_valid(raise_exception=True)):
            p, created = serializer.save(serializer.validated_data)
            if created:
                return JsonResponse(ProfileSerializer(p).data, status=status.HTTP_201_CREATED, safe=False)
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, format=None):
        """
        Change profile info
        """
        profile = request.data
        profile['user'] = request.user.id
        serializer = ProfileSerializer(data=profile, partial=True)

        if (serializer.is_valid(raise_exception=True)):
            p, created = serializer.save(serializer.validated_data)
            if created:
                return JsonResponse(ProfileSerializer(p).data, status=status.HTTP_201_CREATED, safe=False)
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CurrentUserGoal(views.APIView):

    schema = CurrentUserGoalSchema()

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Get user goal
        """
        profile = Profile.objects.get(user=request.user)
        return JsonResponse(GoalSerializer(profile.goal).data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        """
        Add user goal
        """
        profile = request.data
        profile['user'] = request.user.id
        serializer = ProfileSerializer(data=profile, partial=True)

        if (serializer.is_valid(raise_exception=True)):
            p, created = serializer.save(serializer.validated_data)
            if created:
                return JsonResponse(ProfileSerializer(p).data, status=status.HTTP_201_CREATED, safe=False)
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, format=None):
        """
        Change user goal
        """
        profile = request.data
        profile['user'] = request.user.id
        serializer = ProfileSerializer(data=profile, partial=True)

        if (serializer.is_valid(raise_exception=True)):
            p, created = serializer.save(serializer.validated_data)
            if created:
                return JsonResponse(ProfileSerializer(p).data, status=status.HTTP_201_CREATED, safe=False)
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CurrentUserCategory(views.APIView):

    schema = CurrentUserCategorySchema()

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Get list of current users categories
        """
        response = []
        categories = UserCategory.objects.filter(user=request.user)
        for category in categories:
            response.append(UserCategorySerializer(category).data)

        return JsonResponse(response, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):

        """
        Add categories for current user. List of added categories looks like ['peanut', 'sugar', 'milk', 'egg'].
        """
        categories = request.data['categories']
        result = []
        for category in categories:
            serializer = UserCategorySerializer(data={'user': request.user.id,
                                                      'category': get_choice(category, CATEGORY_CHOICES)})
            if (serializer.is_valid(raise_exception=True)):
                ctgr, created = serializer.save(serializer.validated_data)
                if created:
                    result.append(UserCategorySerializer(ctgr).data)

        return JsonResponse(result, status=status.HTTP_201_CREATED, safe=False)

    def put(self, request, format=None):
        """
        Add categories for current user. List of added categories looks like ['peanut', 'sugar', 'milk', 'egg'].
        """
        categories = request.data['categories']
        result = []
        for category in categories:

            serializer = UserCategorySerializer(data={'user': request.user.id,
                                                      'category': category})
            if (serializer.is_valid()):
                ctgr, created = serializer.save(serializer.validated_data)
                if created:
                    result.append(UserCategorySerializer(ctgr).data)

        return JsonResponse(result, status=status.HTTP_201_CREATED, safe=False)

    def delete(self, request, format=None):

        """
        Delete categories for current user. List of categories looks like ['peanut', 'sugar', 'milk', 'egg'].
        """
        categories = request.data['categories']
        for category in categories:
            ctgr = get_choice(category, CATEGORY_CHOICES)
            ctgr = UserCategory.objects.get(Q(user_id=request.user.id), Q(category=ctgr)).delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CurrentUserIngredient(views.APIView):

    schema = CurrentUserIngredientSchema()

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Get list of current users ingredients
        """
        response = []
        ingredients = UserIngredient.objects.filter(user=request.user)
        for ingredient in ingredients:
            response.append(UserIngredientSerializer(ingredient).data)

        return JsonResponse(response, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        """
        Add ingredients for current user
        """
        ingredients = request.data['ingredients']
        result = []
        for ingredient in ingredients:
            serializer = UserIngredientSerializer(data={'user': request.user.id,
                                                        'ingredient': ingredient})
            if (serializer.is_valid(raise_exception=True)):
                ctgr, created = serializer.save(serializer.validated_data)
                if created:
                    result.append(UserIngredientSerializer(ctgr).data)

        return JsonResponse(result, status=status.HTTP_201_CREATED, safe=False)

    def put(self, request, format=None):
        """
        Add ingredients for current user
        """
        ingredients = request.data['ingredients']
        result = []
        for ingredient in ingredients:
            serializer = UserIngredientSerializer(data={'user': request.user.id,
                                                        'ingredient': ingredient})
            if (serializer.is_valid()):
                ctgr, created = serializer.save(serializer.validated_data)
                if created:
                    result.append(UserIngredientSerializer(ctgr).data)

        return JsonResponse(result, status=status.HTTP_201_CREATED, safe=False)
