from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.views import APIView
from django.db.models import Q
from CloudKit.serializers import *
from CloudKit.models import FoodStyle
# Create your views here.

class Home(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": 200,
            "error" : "",
            "data": {
                "message": "Success message from server",
            }
        })
    
class FoodStyle(APIView):
    def get(self,request):
        query = request.GET.get('id')
        if query:
            food_styles = FoodStyle.objects.filter(
                Q(id=query) |
                Q(name__icontains=query) |
                Q(region__name__icontains=query)  # Assuming region is a ForeignKey to a Regions model
                )
        else:
            food_styles = FoodStyle.objects.all()
        
        serializer=FoodStyleSerializer(food_styles,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=FoodStyleSerializer(data=request.data)
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
    def delete(self,request):
        pk = request.GET.get('pk')
        food_style = get_object_or_404(FoodStyle, pk=pk)
        food_style.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Category(APIView):
    def get(self,request):
        query = request.GET.get('id')
        if query:
            food_styles = FoodStyle.objects.filter(
                Q(id=query) |
                Q(name__icontains=query) |
                Q(region__name__icontains=query)  # Assuming region is a ForeignKey to a Regions model
                )
        else:
            food_styles = Category.objects.all()
        
        serializer=CategorySerializer(food_styles,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        pk = request.GET.get('pk')
        food_style = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(food_style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        pk = request.GET.get('pk')
        food_style = get_object_or_404(Category, pk=pk)
        food_style.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
