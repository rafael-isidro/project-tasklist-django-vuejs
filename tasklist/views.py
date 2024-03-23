from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .models import Tasklist
from .serializers import TasklistSerializer

class ListCreateTasklist(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = TasklistSerializer

    def get_queryset(self):
        return Tasklist.objects.filter(user=self.request.user)