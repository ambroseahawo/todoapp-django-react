"""Define database models"""

from django.db import models

# Create your models here.

class Todo(models.Model):
    """Define todos table"""
    activity = models.CharField(max_length=20, unique=True)
    # slug = models.SlugField(unique=True, default=uuid.uuid1)
    reminder = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    activity_datetime = models.DateField()
    # housekeeping
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['activity_datetime']
