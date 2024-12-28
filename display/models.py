from django.db import models
from datetime import datetime

# Create your models here.
class Session(models.Model):
    beganAt = models.DateTimeField()
    length = models.FloatField()

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    createdAt = models.DateTimeField(default=datetime.now())
    sessions = models.ManyToManyField(Session)