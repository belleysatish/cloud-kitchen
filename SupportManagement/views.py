from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from SupportManagement.models import *
from SupportManagement.serializer import *
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

class Tickets(APIView):


    def get(self,request):
        query=TicketingSystem.objects.all()
        serializer=TicketingSystemSerializer(query,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer=TicketingSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request):
        query=request.GET.get(id,query)
        output=get_object_or_404(TicketingSystem,id=query)
        output.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ExperienceSupport(APIView):

    def get(Self,request):
        query = SupportExperience.objects.all()
        serializer=SupportExperienceSerializer(query,many=True)
        return Response(serializer.data)
    def post(Self,request):
        serializer=SupportExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    

    
    



        