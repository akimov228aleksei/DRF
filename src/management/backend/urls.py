from django.urls import path, include
from .views import department


urlpatterns = [
    # path('drf-auth', include('rest_framework.urls')),
    path('departmentlist/', department.DepartmentAPIView.as_view()),
    path('departmentdetail/<int:pk>', department.DepartmentAPIView.as_view()),
]