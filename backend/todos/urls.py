from django.urls import path
from todos.views import TodosListView, TodoDetailView

app_name = 'todos'

urlpatterns = [
    path('<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('', TodosListView.as_view(), name='index')
]

