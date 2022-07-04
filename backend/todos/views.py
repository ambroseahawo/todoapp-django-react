"""define how web requests are taken and responded to"""
from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
class TodosListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)
    
    def post (self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get_object(self, pk):
        todo = get_object_or_404(Todo, id=pk)
        return todo

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        # print("Serializer => {0}".format(serializer.data))
        return Response(serializer.data)

    def put(self, request, pk):
        print("Request data => {0}".format(request.data))
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(data={"detail": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
