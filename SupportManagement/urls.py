from django.urls import path
from SupportManagement.views import *
urlpatterns = [
    path('ratings/', ExperienceSupport.as_view(), name='rating'),
    path('tickets/', Tickets.as_view(), name='Tickets'),
]
