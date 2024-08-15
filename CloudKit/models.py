from django.db import models

from LocationManagement.models import Regions
from user.models import DefaultModel

class FoodStyle(DefaultModel, models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    region = models.ManyToManyField(Regions, related_name="food_style")
    # when_to_show = models.IntegerField()
    avatar = models.URLField()
    description = models.TextField()
    data = models.JSONField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'FOODSTYLE'
    
class Category(DefaultModel, models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    food_style = models.ManyToManyField(FoodStyle, related_name="category")
    # when_to_show = models.IntegerField()
    avatar = models.URLField()
    description = models.TextField()
    #data = models.JSONField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'CATEGORY'

class Meal(DefaultModel, models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name="meal")
    # when_to_show = models.IntegerField()
    rating=models.IntegerField()
    avatar = models.URLField()
    description = models.TextField()
    data = models.JSONField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'MEAL'

class Items(DefaultModel, models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # max_setable_items = models.IntegerField()
    number_of_units = models.IntegerField()
    unit_price = models.IntegerField()
    meal = models.ManyToManyField(Meal, blank=True, related_name = 'items')
    # when_to_show = models.IntegerField()
    avatar = models.URLField()
    description = models.TextField()
    data = models.JSONField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'ITEMS'


    