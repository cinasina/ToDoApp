from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from todo.models import TodoModel


class Command(BaseCommand):
    help = "Inserting Data"

    def handle(self, *args, **options):
        self.fake = Faker()
        for _ in range(5):
            user = User.objects.create_user(email=self.fake.email(), password="asd34asd")
            profile = Profile.objects.get(user=user)
            task = TodoModel.objects.create(
                user=user, title=self.fake.word(),
                description=self.fake.text(max_nb_chars=7),
                is_done=self.fake.boolean()
            )
            print(task.user, task.title, task.description, task.is_done)


