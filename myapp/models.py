from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
# default=timezone.now

#class Todotime(models.Model):
    #time = models.TimeField(auto_now_add=True, blank=True)

class TodoModels(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    time = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
