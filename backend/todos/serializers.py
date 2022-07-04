"""Define data passed via the rest api"""

from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """define todo serializer"""
    class Meta:
        """specify which model to use and what fields to serialize"""
        model = Todo
        fields = ['activity', 'reminder', 'completed', 'activity_datetime']
