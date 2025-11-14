from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=30)

    # To represent objects of the models with human readable name
    def __str__(self):
        return self.name

class Result(models.Model):
    stu_class = models.CharField(max_length=70)
    marks = models.IntegerField()

    def __str__(self):
        return self.stu_class