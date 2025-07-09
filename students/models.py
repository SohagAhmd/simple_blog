from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brach = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name