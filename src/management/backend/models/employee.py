from django.db import models
from .department import Department
from .position import Position
from django.utils.timezone import now


class Employee(models.Model):
    """Class containing fields and methods of the model"""

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    birthday = models.DateField()
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    position = models.ForeignKey(Position, null=True, on_delete=models.SET_NULL)
    salary = models.PositiveIntegerField()
    on_boarding_day = models.DateField(default=now)

    def __str__(self):
        return self.first_name
