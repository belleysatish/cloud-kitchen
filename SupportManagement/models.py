from django.db import models
from user.models import User
from CloudKit.models import Meal

class TicketingSystem(models.Model):
    CATEGORY_CHOICES = [
        ('Order Issues', 'Order Issues'),
        ('Delivery Issues', 'Delivery Issues'),
        ('Payment Issues', 'Payment Issues'),
        ('General Inquiries', 'General Inquiries'),
    ]
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    assigned_to = models.ForeignKey(User, related_name='assigned_tickets', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class SupportExperience(models.Model):
    order = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], help_text="Rate your experience from 1 to 5")
    comments = models.TextField(blank=True, null=True, help_text="Provide detailed feedback")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"

    class Meta:
        ordering = ['-created_at']
