from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import Task, Committee

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    committee = serializers.SlugRelatedField(
            queryset=Committee.objects.all(), 
            slug_field="name"
    )

    class Meta:
        model = Task
        fields = ('url', 'id', 'committee', 'description', 'status', 'due_date')

class CommitteeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Committee
        fields = ('url', 'id', 'name', 'head', 'members')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name')