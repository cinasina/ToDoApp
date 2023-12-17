from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from todo.models import TodoModel


class TodoView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@test.com', password='asd34asd')
        self.todo = TodoModel.objects.create(
            user=self.user,
            title='Test Create User',
            description='Test Model Create',
            is_done=True,
        )

    def test_todo_view_url_task_list_response_200(self):
        url = reverse('todo_app:task_list')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_todo_view_url_update_todo_response_200(self):
        url = reverse('todo_app:update_task', kwargs={'pk': self.todo.pk})
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
