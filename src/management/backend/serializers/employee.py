from rest_framework import serializers
from ..models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Data serialization class for the whole list of records"""

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'second_name', 'department', 'position')


class EmployeeDetailSerializer(serializers.ModelSerializer):
    """Single entry data serialization class"""

    class Meta:
        model = Employee
        fields = '__all__'
