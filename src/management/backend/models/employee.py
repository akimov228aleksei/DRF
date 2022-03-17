from django.db import models
from .department import Department
from datetime import date


class Employee(models.Model):
    first_name = models.Charfield(max_lenght=100)
    second_name = models.CharField(max_lenght=100)
    birthday = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    on_boarding_day = models.DateField(default=date.today())

    def __str__(self):
        return self.first_name
