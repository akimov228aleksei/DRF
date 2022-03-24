from rest_framework import serializers
from ..models.department import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('title', 'description')


class DepartmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    total_count_employee = serializers.IntegerField()
    average_salary = serializers.IntegerField()