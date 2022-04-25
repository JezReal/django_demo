from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
