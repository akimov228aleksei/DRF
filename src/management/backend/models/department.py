from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def amount(self):
        from .employee import Employee
        return len(Employee.objects.filter(department=self.pk))

    @property
    def average_salary(self):
        from .employee import Employee
        employee = Employee.objects.filter(department=self.pk)
        return round(sum([i.salary for i in employee])/len(employee))

    def __str__(self):
        return self.title
