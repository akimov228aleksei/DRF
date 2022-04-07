from rest_framework import serializers
from ..models.vacation import Vacation


class VacationSerializer(serializers.ModelSerializer):
    """Data serialization class for the whole list of records"""

    class Meta:
        model = Vacation
        fields = '__all__'
