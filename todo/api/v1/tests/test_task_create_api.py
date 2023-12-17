import pytest
from rest_framework.test import APIClient
from django.shortcuts import reverse
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture()
def my_user():
    user = User.objects.create_user(email='admin@admin.com', password='asd34asd', is_verified=True, is_active=True)
    return user


@pytest.fixture()
def auth_client(my_user):
    client = APIClient()
    token = RefreshToken.for_user(my_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
    return client


@pytest.mark.django_db
class TestTaskAPI:

    def test_get_response_200_status(self, auth_client):
        url = reverse('todo_app:v1.api.todo:api_task_list_create')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_post_create_status_201(self, my_user, auth_client):
        data = {
            'user': my_user.pk,
            'title': 'test',
            'description': 'testing',
            'is_done': True,
        }
        url = reverse('todo_app:v1.api.todo:api_task_list_create')
        response = auth_client.post(url, data)
        assert response.status_code == 201