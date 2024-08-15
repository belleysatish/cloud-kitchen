from django.urls import path
from SupportManagement.views import *
urlpatterns = [
    path('/tickets',Tickets.as_view(),name='Tickets'),
    path('/ratings',ExperienceSupport.as_view(),name='rating'),
]
