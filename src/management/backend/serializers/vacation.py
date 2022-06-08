from rest_framework import serializers
from ..models.vacation import Vacation


class VacationSerializer(serializers.HyperlinkedModelSerializer):
    """Data serialization class for the whole list of records"""
    employee = serializers.CharField()
    employee_second_name = serializers.CharField(source='employee.second_name')

    class Meta:
        model = Vacation
        fields = ('url', 'employee', 'employee_second_name', 'start_date', 'end_date')


class VacationDetailSerializer(serializers.ModelSerializer):
    """Single entry data serialization class"""
    employee_first_name = serializers.CharField(source='employee.first_name', read_only=True)
    employee_second_name = serializers.CharField(source='employee.second_name', read_only=True)

    class Meta:
        model = Vacation
        fields = '__all__'
