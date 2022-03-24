from django.db import models


class Position(models.Model):
    """Class containing fields and methods of the model"""

    title = models.CharField(max_length=100, unique=True)
    max_salary = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
