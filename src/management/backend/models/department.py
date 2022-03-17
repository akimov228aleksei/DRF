from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    @property
    def amount(self):
        pass

    @property
    def average_salary(self):
        pass

    def __str__(self):
        return self.title
