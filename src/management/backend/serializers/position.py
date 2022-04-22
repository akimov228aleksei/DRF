from rest_framework import serializers
from ..models.position import Position


class PositionSerializer(serializers.ModelSerializer):
    """Data serialization class for the whole list of records"""

    class Meta:
        model = Position
        fields = ('url', 'title', 'max_salary', 'active', 'time_create')
