from django.urls import path, include
from .views import department


urlpatterns = [
    # path('drf-auth', include('rest_framework.urls')),
    path('departmentlist/', department.DepartmentViewSet.as_view({'get': 'list',
                                                                  'post':'create'})),
    path('departmentdetail/<int:pk>', department.DepartmentViewSet.as_view({'get': 'retrieve',
                                                                            'put': 'update',
                                                                            'delete': 'destroy'})),
]