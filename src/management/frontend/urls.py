"""Module with Frontend URL ratios"""

from django.urls import path
from frontend.views import department, employee
from frontend.views.auth import registration, authorization, logout

urlpatterns = [
    # Department urls
    path('', department.DepartmentListView.as_view(), name='home'),
    path('department/update', department.DepartmentUpdateView.as_view(), name='department-update'),
    path('department/delete', department.DepartmentDeleteView.as_view(), name='department-delete'),
    path('department/create', department.DepartmentCreateView.as_view(), name='department-create'),
    # Employee urls
    path('employee/list', employee.EmployeeListView.as_view(), name='employee-list'),
    # Auth urls
    path('authorization/', authorization.AuthorizationView.as_view(), name='authorization'),
    path('registration/', registration.RegistrationView.as_view(), name='registration'),
    path('logout/', logout.LogoutView.as_view(), name='logout'),
]
