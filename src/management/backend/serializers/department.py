from rest_framework import serializers
from ..models.department import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Data serialization class for the whole list of records"""

    class Meta:
        model = Department
        fields = ('id', 'title', 'description')


class DepartmentDetailSerializer(serializers.ModelSerializer):
    """Single entry data serialization class"""

    class Meta:
        model = Department
        fields = '__all__'

    total_count_employee = serializers.IntegerField()
    average_salary = serializers.IntegerField()
