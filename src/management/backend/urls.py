from django.urls import path, include
from .views import department


urlpatterns = [
    # path('drf-auth', include('rest_framework.urls')),
    path('departmentlist/', department.DepartmentView.as_view()),
    path('departmentdetail/<int:pk>', department.DepartmentView.as_view()),
]