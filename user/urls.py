from django.urls import path
from user.views import UserLoginAPIView, UserLogoutAPIView, UserAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path('users/', UserAPIView.as_view(), name='user_list'),
    
]
