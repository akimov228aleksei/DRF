"""Module with Frontend URL ratios"""

from django.urls import path
from frontend.views import department, employee, position, vacation
from frontend.views.auth import registration, authorization, logout

urlpatterns = [
    # Department urls
    path('', department.DepartmentListView.as_view(), name='home'),
    path('department/update', department.DepartmentUpdateView.as_view(), name='department-update'),
    path('department/delete', department.DepartmentDeleteView.as_view(), name='department-delete'),
    path('department/create', department.DepartmentCreateView.as_view(), name='department-create'),
    path('department/detail', department.DepartmentDetailView.as_view(), name='department-detail'),
    # Employee urls
    path('employee/list', employee.EmployeeListView.as_view(), name='employee-list'),
    path('employee/create', employee.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/update', employee.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/delete', employee.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('employee/detail', employee.EmployeeDetailView.as_view(), name='employee-detail'),
    # Position urls
    path('position/list', position.PositionListView.as_view(), name='position-list'),
    path('position/create', position.PositionCreateView.as_view(), name='position-create'),
    path('position/update', position.PositionUpdateView.as_view(), name='position-update'),
    path('position/delete', position.PositionDeleteView.as_view(), name='position-delete'),
    # Vacation urls
    path('vacation/list', vacation.VacationListView.as_view(), name='vacation-list'),
    path('vacation/create', vacation.VacationCreateView.as_view(), name='vacation-create'),
    path('vacation/update', vacation.VacationUpdateView.as_view(), name='vacation-update'),
    path('vacation/delete', vacation.VacationDeleteView.as_view(), name='vacation-delete'),
    # Auth urls
    path('authorization/', authorization.AuthorizationView.as_view(), name='authorization'),
    path('registration/', registration.RegistrationView.as_view(), name='registration'),
    path('logout/', logout.LogoutView.as_view(), name='logout'),
]
