from django.urls import path, include
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.TasksList.as_view(), name='task_list'),
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('update/<int:pk>/', views.UpdateTaskView.as_view(), name='update_task'),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('api/v1/', include('todo.api.v1.urls'), name='v1.api.todo'),
]