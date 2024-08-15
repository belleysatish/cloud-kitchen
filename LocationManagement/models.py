from django.db import models

from user.models import DefaultModel

# Create your models here.

class Regions(DefaultModel, models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"
    
    class Meta:
        db_table = "REGIONS"

