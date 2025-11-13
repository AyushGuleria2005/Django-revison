from email.policy import default
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    division = models.CharField(max_length=2)
    usn = models.CharField(max_length=15)
    activeKt = models.BooleanField(default=False)

