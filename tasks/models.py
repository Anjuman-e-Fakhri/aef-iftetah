from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Committee(models.Model):
	name = models.CharField(max_length=30)
	head = models.ForeignKey(User, on_delete="CASCADE", related_name="head")
	members = models.ManyToManyField(User, related_name="members")

	def __str__(self):
		return self.name


class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    description = models.CharField(max_length=250)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    committee = models.ForeignKey(Committee, on_delete="CASCADE")

    class Meta:
        ordering = ['committee', 'due_date', 'status']

    def __str__(self):
        return "{} - {}".format(self.committee, self.description)
