from rest_framework import serializers
from ..models.department import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """Data serialization class for the whole list of records"""

    class Meta:
        model = Department
        fields = ('url', 'title', 'description')


class DepartmentDetailSerializer(serializers.ModelSerializer):
    """Single entry data serialization class"""

    class Meta:
        model = Department
        fields = ('url', 'title', 'description', 'time_create', 'time_update',
                  'total_count_employee', 'average_salary')

    total_count_employee = serializers.IntegerField()
    average_salary = serializers.IntegerField()
