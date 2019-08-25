from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import City, Category, Guide


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = City
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    description = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'description',)


class GuideSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phrase = serializers.CharField()
    photo = serializers.CharField()
    facebook = serializers.CharField()
    instagram = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    city = CitySerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Guide
        fields = ('name', 'phrase', 'photo', 'facebook', 'instagram', 'phone', 'email', 'city', 'category')



