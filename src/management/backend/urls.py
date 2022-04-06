from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import department
from .views import department, employee

router = SimpleRouter()
router.register(r'department', department.DepartmentViewSet, basename='department')
router.register(r'employee', employee.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]