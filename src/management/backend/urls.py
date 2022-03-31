from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import department
from .views.department import DepartmentViewSet

router = SimpleRouter()
router.register(r'department', DepartmentViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls)),
]