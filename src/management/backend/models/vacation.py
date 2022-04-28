from datetime import date
from django.db import models


class Vacation(models.Model):
    """Class containing fields and methods of the model"""

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

    def __str__(self):
        return self.employee.first_name
