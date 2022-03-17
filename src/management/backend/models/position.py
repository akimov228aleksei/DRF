from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100)
    max_salary = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
