from django.contrib import admin
from backend.models import department, employee, position, vacation
# Register your models here.

admin.site.register(department.Department)
admin.site.register(employee.Employee)
admin.site.register(position.Position)
admin.site.register(vacation.Vacation)
