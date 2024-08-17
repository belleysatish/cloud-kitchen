from django.urls import path
from SupportManagement.views import Tickets, ExperienceSupport
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tickets/', Tickets.as_view(), name='tickets_list_create'),
    path('tickets/<int:pk>/', Tickets.as_view(), name='ticket_detail'),
    path('ratings/', ExperienceSupport.as_view(), name='ratings_list_create'),
    path('ratings/<int:pk>/', ExperienceSupport.as_view(), name='rating_detail'),
]
