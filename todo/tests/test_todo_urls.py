from django.test import TestCase
from django.urls import reverse, resolve
from ..views import CreateTaskView


class TestUrl(TestCase):
    def test_create_task_url_resolve(self):
        url = reverse('todo_app:create_task')
        self.assertEqual(resolve(url).func.view_class, CreateTaskView)
