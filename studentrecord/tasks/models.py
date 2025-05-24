from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    age = models.IntegerField()
    roll_num = models.IntegerField(unique=True)
    marks = models.FloatField()
    grade = models.CharField(max_length=5, default='C')  # Added with default value

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_num})"
