from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Committee(models.Model):
    name = models.CharField(max_length=30)
    heads = models.ManyToManyField(User, related_name="heads", blank=True)
    members = models.ManyToManyField(User, related_name="members", blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    description = models.CharField(max_length=250)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    committee = models.ForeignKey(Committee, on_delete="CASCADE")
    assigned = models.ForeignKey(User, on_delete="SET_NULL", null=True, blank=True)

    class Meta:
        ordering = ['committee', 'due_date', 'status']

    def __str__(self):
        return "{} - {}".format(self.committee, self.description)
