from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from ..models.employee import Employee
from ..serializers.employee import EmployeeSerializer, EmployeeDetailSerializer


class EmployeeViewSet(ViewSet):
    """A class that describes all available methods with a employee model"""

    def list(self, request):
        """The method displays all records"""
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True,
                                        context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """The method displays the detailed data of a particular record"""
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data)

    def create(self, request):
        """The method creates a new record"""
        serializer = EmployeeDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        """The method updates a specific record"""
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeDetailSerializer(data=request.data,
                                              instance=employee)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """The method deletes a specific entry"""
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeDetailSerializer(instance=employee)
        employee.delete()
        return Response(serializer.data)
