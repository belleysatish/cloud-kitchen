from django.urls import path
from LocationManagement.views import *

urlpatterns = [
    path('', LocationCRUDOPerations.as_view(), name='CRUD_location')
]
