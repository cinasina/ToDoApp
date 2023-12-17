from django.test import TestCase
from ..models import TodoModel
from accounts.models import User


class TestTodoModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='asd34asd')
        self.todo = TodoModel.objects.create(
            user=self.user,
            title='Test Create User',
            description='Test Model Create',
            is_done=True,
        )

    def test_create_task(self):

        self.assertTrue(TodoModel.objects.filter(pk=self.todo.id).exists())
