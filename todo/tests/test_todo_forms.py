from django.test import SimpleTestCase
from ..forms import TodoForm


class TestTodoForm(SimpleTestCase):
    def test_form_with_data_valid(self):
        form = TodoForm(data={
            'title': 'Test Form',
            'description': 'I am Testing Form'
        })
        self.assertTrue(form.is_valid())
