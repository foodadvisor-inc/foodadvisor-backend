from rest_framework import serializers

from api.models import *


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'



class UserCategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display')
    class Meta:
        model = UserCategory
        fields = '__all__'

    def save(self, validated_data):
        user = validated_data.pop('user')
        current_category = validated_data.pop('get_category_display')
        instance, created = UserCategory.objects.update_or_create(user=user, category=current_category, defaults=validated_data)
        return instance, created


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'user': {'validators': []},
        }


    def save(self, validated_data):
        user = validated_data.pop('user')
        instance, created = Profile.objects.update_or_create(user=user, defaults=validated_data)
        return instance,created





class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    # TODO: create verifications

