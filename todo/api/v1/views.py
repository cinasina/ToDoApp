from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TodoSerializer
from ...models import TodoModel
from rest_framework.permissions import IsAuthenticated


class ListTodoView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = TodoModel.objects.filter(user_id=user_id)
        return queryset


class DetailAndUpdateTodoView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = TodoModel.objects.get(pk=self.kwargs['pk'], user=self.request.user)
        return obj
