from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.title}'
