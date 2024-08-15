from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication 
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from user.models import *
from django.contrib.auth import get_user_model
from django.db.models import Q

user=get_user_model()

def api_url(request):
    urls={
        "UserLoginAPIView" : "/login/",
        "UserLogoutAPIView" : "/logout/",
        "UserAPIView" : "/users/",
    }

class UserLoginAPIView(APIView):
    authentication_classes=(BasicAuthentication)
    permission_classes=(IsAuthenticated)

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        
        if request.user.is_authenticated:
            user_data = {
                'username': request.user.username,
                'email': request.user.email,
                'crated at' : request.user.created_at,
                # Add more user-related data as needed
            }
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User is not logged in'}, status=status.HTTP_401_UNAUTHORIZED)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None:
            return Response({'message':'please provide username'})
        elif password is None:
            return Response({'message':'Please Provide Password'})
        else:
            authentication = authenticate(username=username, password=password)
            if authentication is not None:
                login(request, authentication)
                data = UserSerializer(request.user)
                return Response({'message': 'Login successful','user_details':data.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutAPIView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User not logged in'}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    authentication_classes=(BasicAuthentication)
    permission_classes=[IsAuthenticated]

    @method_decorator(csrf_exempt)
    def get(self, request, format=None): #queryperms
        query=request.GET.get('user_id') #filter users based on emailid ,username,user_id
        user = get_object_or_404(user, )
        serializer = UserSerializer(user)
        return Response(serializer.data)
    #password should not go to fd in get but should able to change the password using put
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @method_decorator(csrf_exempt)
    def put(self, request):
        pk=request.GET.get('user_id',pk)
        user = get_object_or_404(user, id=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @method_decorator(csrf_exempt)
    def delete(self, request):
        pk=request.GET.get('user_id',pk)
        user = get_object_or_404(user, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
