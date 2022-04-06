from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import department
from .views import department, employee, position

router = SimpleRouter()
router.register(r'department', department.DepartmentViewSet, basename='department')
router.register(r'employee', employee.EmployeeViewSet, basename='employee')
router.register(r'position', position.PositionViewSet, basename='position')

urlpatterns = [
    path('', include(router.urls)),
]