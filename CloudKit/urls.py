from django.contrib import admin
from . import views
from django.urls import path,include
from CloudKit.views import Home, FoodStyleView, CategoryView, MealView, ItemView

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('home/', Home.as_view(), name='home'),
    path('foodstyle/', FoodStyleView.as_view(), name='foodstyle_list_create'),
    path('category/', CategoryView.as_view(), name='category_list_create'),
    path('meal/', MealView.as_view(), name='meal_list_create'),
    path('item/', ItemView.as_view(), name='item_list_create'),
    path('user/', include('user.urls')),
    path('location/', include('LocationManagement.urls')),
    path('support/', include('SupportManagement.urls')),
]
