from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Tasklist
from .serializers import TasklistSerializer

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "user_id": user.id})

# GetAll and Create Tasklist
class ListCreateTasklist(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = TasklistSerializer

    def get_queryset(self):
        return Tasklist.objects.filter(user=self.request.user)

# Get, Update and Delete Tasklist
class RetrieveUpdateDestroyTasklist(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer