from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=220)
    age=models.IntegerField()
    address=models.CharField(max_length=220)
    mark=models.IntegerField()



class Teacher(models.Model):
    name=models.CharField(max_length=220)
    age=models.IntegerField()
    address=models.CharField(max_length=220)
    

    def __str___(self):
        return self.name