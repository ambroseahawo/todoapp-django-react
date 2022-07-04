"""define how web requests are taken and responded to"""
from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TodosListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)
