from django.db import models

# Create your models here.
class Todo(models.Model):
    activity = models.CharField(max_length=20)
    reminder = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    activity_datetime = models.DateField()
    # housekeeping
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
