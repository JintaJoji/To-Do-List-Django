from django.db import models

# Create your models here.
class Task(models.Model):
    tasktodo=models.CharField(max_length=75)