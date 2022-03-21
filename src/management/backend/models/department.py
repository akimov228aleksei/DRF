from django.db import models
from .employee import Employee
from django.db.models import Count, Avg


class Department(models.Model):
    """Class containing fields and methods of the model"""

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    @property
    def total_count_employee(self):
        """A function that counts the number of employees in each department"""

        count = Department.objects.annotate(Count('employee')).filter(pk=self.pk)

        return count[0].employee__count if count else 0

    @property
    def average_salary(self):
        """A function that calculates the average salary of each department"""

        salary = Employee.objects.values('department_id').annotate(salary=Avg('salary')).filter(department_id=self.pk)

        return salary[0]['salary'] if salary else 0

    def __str__(self):
        return self.title
