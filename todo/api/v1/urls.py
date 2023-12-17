from django.urls import path
from . import views

app_name = 'v1.api.todo'

urlpatterns = [
    path('', views.ListTodoView.as_view(), name='api_task_list_create'),
    path('detail/<int:pk>/', views.DetailAndUpdateTodoView.as_view(), name='api_task_list_delete_update_detail'),
]
