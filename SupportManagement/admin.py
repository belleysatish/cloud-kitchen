from django.contrib import admin
from SupportManagement.models import *
from CloudKit.models import *
# Register your models here.
admin.site.register(TicketingSystem)
admin.site.register(SupportExperience)
admin.site.register(Category)
admin.site.register(Meal)