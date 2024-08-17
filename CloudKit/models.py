from django.db import models
from LocationManagement.models import Regions
from user.models import DefaultModel

class FoodStyle(DefaultModel):
    name = models.CharField(max_length=50)
    region = models.ManyToManyField(Regions, related_name="food_styles")
    avatar = models.URLField()
    description = models.TextField()
    data = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'foodstyle'
    
class Category(DefaultModel):
    name = models.CharField(max_length=50)
    food_style = models.ManyToManyField(FoodStyle, related_name="categories")
    avatar = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class Meal(DefaultModel):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name="meals")
    rating = models.IntegerField()
    avatar = models.URLField()
    description = models.TextField()
    data = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'meal'

class Item(DefaultModel):
    name = models.CharField(max_length=100)
    number_of_units = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    meal = models.ManyToManyField(Meal, related_name='items', blank=True)
    avatar = models.URLField()
    description = models.TextField()
    data = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item'
