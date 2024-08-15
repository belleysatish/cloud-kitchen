from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from LocationManagement.models import *
from LocationManagement.serializers import *
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class LocationCRUDOPerations(APIView):

    def get(self,request):
        queryset=Regions.objects.all()
        serializer=LocationCRUDSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=LocationCRUDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #unable to perform put and delete operations
    def put(self, request, pk=None):
        pk = request.GET.get('user_id', pk)
        user = get_object_or_404(Regions, id=pk)
        serializer = LocationCRUDSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        pk = request.GET.get('Region_id', pk)
        region = get_object_or_404(Regions, id=pk)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class get_location_show_restaurants(APIView):
    def get(self,request):
        location=request.GET.get('location')

