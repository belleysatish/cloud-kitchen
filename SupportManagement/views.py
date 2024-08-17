from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render
from SupportManagement.models import TicketingSystem, SupportExperience
from SupportManagement.serializer import TicketingSystemSerializer, SupportExperienceSerializer

def index(request):
    return render(request, 'SupportManagement\index.html')

class Tickets(APIView):
    
    def get(self, request):
        tickets = TicketingSystem.objects.all()
        serializer = TicketingSystemSerializer(tickets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TicketingSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        ticket = get_object_or_404(TicketingSystem, pk=pk)
        serializer = TicketingSystemSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        ticket = get_object_or_404(TicketingSystem, pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ExperienceSupport(APIView):

    def get(self, request):
        experiences = SupportExperience.objects.all()
        serializer = SupportExperienceSerializer(experiences, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SupportExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        experience = get_object_or_404(SupportExperience, pk=pk)
        serializer = SupportExperienceSerializer(experience, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        experience = get_object_or_404(SupportExperience, pk=pk)
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
