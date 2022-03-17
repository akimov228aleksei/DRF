from django.db import models
from .employee import Employee
from datetime import date


class Vacation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today())
    end_date = models.DateField()

    def __str__(self):
        return self.employee.name
