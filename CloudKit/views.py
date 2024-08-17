from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from CloudKit.serializers import FoodStyleSerializer, CategorySerializer, MealSerializer, ItemSerializer
from CloudKit.models import FoodStyle, Category, Meal, Item

class Home(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": 200,
            "message": "Success message from server",
        })
    
def home(request):
    return render(request, 'cloudkit\home.html')


class FoodStyleView(APIView):
    def get(self, request):
        query = request.GET.get('id')
        if query:
            food_styles = FoodStyle.objects.filter(
                Q(id=query) | Q(name__icontains=query) | Q(region__name__icontains=query)
            )
        else:
            food_styles = FoodStyle.objects.all()
        
        serializer = FoodStyleSerializer(food_styles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodStyleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('pk')
        food_style = get_object_or_404(FoodStyle, pk=pk)
        serializer = FoodStyleSerializer(food_style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('pk')
        food_style = get_object_or_404(FoodStyle, pk=pk)
        food_style.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryView(APIView):
    def get(self, request):
        query = request.GET.get('id')
        if query:
            categories = Category.objects.filter(
                Q(id=query) | Q(name__icontains=query)
            )
        else:
            categories = Category.objects.all()
        
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('pk')
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('pk')
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MealView(APIView):
    def get(self, request):
        query = request.GET.get('id')
        if query:
            meals = Meal.objects.filter(
                Q(id=query) | Q(name__icontains=query)
            )
        else:
            meals = Meal.objects.all()
        
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('pk')
        meal = get_object_or_404(Meal, pk=pk)
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('pk')
        meal = get_object_or_404(Meal, pk=pk)
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemView(APIView):
    def get(self, request):
        query = request.GET.get('id')
        if query:
            items = Item.objects.filter(
                Q(id=query) | Q(name__icontains=query)
            )
        else:
            items = Item.objects.all()
        
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('pk')
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('pk')
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
