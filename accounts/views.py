from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class SignupUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('todo_app:task_list')
    template_name = 'accounts/signup.html'


class LoginUser(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('todo_app:task_list')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('todo_app:task_list')



