from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .serializers import *

# Create your views here.

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for groups
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tasks
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
