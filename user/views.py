from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializer import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from user.models import *
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import generics

user = get_user_model()

# Utility function to handle login redirection
def redirect_if_authenticated(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the user dashboard after successful login

# API URL view for easy navigation
def api_url(request):
    urls = {
        "UserLoginAPIView": "/login/",
        "UserLogoutAPIView": "/logout/",
        "UserAPIView": "/users/",
    }
    return Response(urls)

# Login View
class UserLoginAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = []

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Redirect to dashboard if already logged in
        return render(request, 'user/login.html')  # Render login template

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return render(request, 'user/login.html', {'error': 'Please provide both username and password'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard on successful login
        else:
            return render(request, 'user/login.html', {'error': 'Invalid credentials'})

# Logout View
class UserLogoutAPIView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        if request.user.is_authenticated:
            logout(request)
            return redirect('login')  # Redirect to login page after logout
        return Response({'message': 'User not logged in'}, status=status.HTTP_400_BAD_REQUEST)

# User API View for CRUD operations
class UserAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        user_id = request.GET.get('user_id')
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def put(self, request):
        user_id = request.GET.get('user_id')
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def delete(self, request):
        user_id = request.GET.get('user_id')
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully!",
        }, status=status.HTTP_201_CREATED)
    
from django.http import JsonResponse

@csrf_exempt
def registration_page(request):
    if request.method == "GET":
        # Return registration form or page
        return render(request, 'user/register.html')
    return JsonResponse({"detail": "Method \"GET\" not allowed."}, status=405)