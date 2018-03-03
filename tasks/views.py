from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .api.serializers import TaskSerializer, CommitteeSerializer, UserSerializer
from .models import Task, Committee
# Create your views here.
def tasks(request):
	return render(request, "tasks.html", {})

def committees(request):
    committees = Committee.objects.all()
    context = {
        "committees":committees
    }
    return render(request, "committees.html", context)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommitteeViewSet(viewsets.ModelViewSet):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer