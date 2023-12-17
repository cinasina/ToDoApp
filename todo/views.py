from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksList(LoginRequiredMixin, ListView):
    model = TodoModel
    fields = ('title', 'description',)
    template_name = 'todo/tasks_list.html'
    success_url = reverse_lazy('todo_app:task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = TodoModel.objects.filter(user__exact=self.request.user)
        return context


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = TodoModel
    fields = ('title', 'description',)
    template_name = 'todo/create_task.html'
    success_url = reverse_lazy('todo_app:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = 'todo/update_task.html'
    model = TodoModel
    fields = ('title', 'description', 'is_done',)
    success_url = reverse_lazy('todo_app:task_list')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    template_name = 'todo/confirm_delete.html'
    model = TodoModel
    success_url = reverse_lazy('todo_app:task_list')
