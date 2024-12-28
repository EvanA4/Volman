from django.db import models
from django.utils import timezone

# Create your models here.
class Session(models.Model):
    beganAt = models.DateTimeField()
    length = models.FloatField()

    def __str__(self):
        return f"{self.length} hour(s) at {self.beganAt}"
    

class Volunteer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    createdAt = models.DateTimeField(default=timezone.now)
    sessions = models.ManyToManyField(Session)

    def __str__(self):
        return f"{self.name} ({self.age})"