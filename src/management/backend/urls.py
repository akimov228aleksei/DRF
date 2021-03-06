"""Module with API URL ratios"""

from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import department, employee, position, vacation, user_permissions

router = SimpleRouter()
router.register(r'department', department.DepartmentViewSet, basename='department')
router.register(r'employee', employee.EmployeeViewSet, basename='employee')
router.register(r'position', position.PositionViewSet, basename='position')
router.register(r'vacation', vacation.VacationViewSet, basename='vacation')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('permissions/', user_permissions.GetUserPermissions.as_view())
]
