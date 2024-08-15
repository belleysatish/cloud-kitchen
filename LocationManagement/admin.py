from django.contrib import admin

# Register your models here.
from CloudKit.models import *
from  LocationManagement.models import *
admin.site.register(FoodStyle)
admin.site.register(Regions)