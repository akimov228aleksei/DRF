from django.db import models


class Department(models.Model):
    """Class containing fields and methods of the model"""

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    @property
    def total_count_employee(self):
        """A function that counts the number of employees in each department"""

        from .employee import Employee
        return len(Employee.objects.filter(department=self.pk))

    @property
    def average_salary(self):
        """A function that calculates the average salary of each department"""

        from .employee import Employee
        employee = Employee.objects.filter(department=self.pk)
        if employee:
            return round(sum([i.salary for i in employee]) / len(employee))
        return 0

    def __str__(self):
        return self.title
