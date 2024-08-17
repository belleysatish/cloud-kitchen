from django.urls import path
from user.views import UserLoginAPIView, UserLogoutAPIView, UserAPIView,RegisterView,registration_page

urlpatterns = [
    path('', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path('users/', UserAPIView.as_view(), name='user_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('registration-page/', registration_page, name='registration_page'),
    path('api/register/', RegisterView.as_view(), name='register'),
    
]
