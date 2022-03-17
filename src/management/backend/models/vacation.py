import django.utils.timezone
from django.db import models
from .employee import Employee
from django.utils.timezone import now


class Vacation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)

    def __str__(self):
        return self.employee.first_name
