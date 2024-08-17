from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
import pytz


# Create your models here.


class CustomUser(AbstractUser):
    # Add your custom fields here

    class Meta:
        permissions = (
            ('can_view', 'Can View'),
        )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Use a unique related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Use a unique related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

class User(AbstractUser):
    avatar = models.URLField(blank=True, null=True)
    user_type = models.CharField(max_length=10, default='CUSTOMER')
    can_use_whatsapp = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    valid_till = models.DateField(default=datetime.now(pytz.utc)+timedelta(days=365))
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table  = "USER"


class DefaultModel(models.Model):
    status = models.BooleanField(default=True)
    valid_till = models.DateField(default=datetime.now(pytz.utc)+timedelta(days=365))
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True