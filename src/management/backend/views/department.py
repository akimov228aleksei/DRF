from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from ..models.department import Department
from ..serializers.department import DepartmentSerializer, DepartmentDetailSerializer


class DepartmentViewSet(ViewSet):
    """A class that describes all available methods with a department model"""

    def list(self, request):
        """The method displays all records"""
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True,
                                          context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """The method displays the detailed data of a particular record"""
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentDetailSerializer(department)
        return Response(serializer.data)

    def create(self, request):
        """The method creates a new record"""
        serializer = DepartmentSerializer(data=request.data,
                                          context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        """The method updates a specific record"""
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentSerializer(data=request.data,
                                          instance=department,
                                          context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """The method deletes a specific entry"""
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        # If employee model has references tp dep. model => abort deletion
        is_exist = department.employee_set.exists()
        if is_exist:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = DepartmentDetailSerializer(instance=department)
        department.delete()
        return Response(serializer.data)
