from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers
from tasks_app.models import *

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        # fields = ["task_name"]
        fields = "__all__"
        # exclude = ['url']
