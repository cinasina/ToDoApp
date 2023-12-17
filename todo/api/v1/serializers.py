from ...models import TodoModel
from rest_framework import serializers
from django.shortcuts import reverse


class TodoSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField('get_absolute_url')

    class Meta:
        model = TodoModel
        fields = ('id', 'user', 'title', 'description', 'is_done', 'absolute_url',)

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(
            reverse('todo_app:v1.api.todo:api_task_list_delete_update_detail', kwargs={'pk': obj.pk}))
