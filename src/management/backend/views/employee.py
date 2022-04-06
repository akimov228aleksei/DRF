from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from ..models.employee import Employee
from ..serializers.employee import EmployeeSerializer, EmployeeDetailSerializer


class EmployeeViewSet(ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeDetailSerializer(department)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Employee.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(data=request.data, instance=department)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Employee.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(instance=department)
        department.delete()
        return Response(serializer.data)
