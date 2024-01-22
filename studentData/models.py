from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    sname = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.roll_no} - {self.sname}"
