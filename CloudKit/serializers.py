from rest_framework import serializers
from CloudKit.models import FoodStyle, Category, Meal, Item

class FoodStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodStyle
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
