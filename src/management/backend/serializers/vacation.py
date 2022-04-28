from rest_framework import serializers
from ..models.vacation import Vacation


class VacationSerializer(serializers.HyperlinkedModelSerializer):
    """Data serialization class for the whole list of records"""

    class Meta:
        model = Vacation
        fields = ('url', 'employee', 'start_date', 'end_date')


class VacationDetailSerializer(serializers.ModelSerializer):
    """Single entry data serialization class"""

    class Meta:
        model = Vacation
        fields = '__all__'
