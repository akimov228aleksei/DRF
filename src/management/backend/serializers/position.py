from rest_framework import serializers
from ..models.position import Position


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    """Data serialization class for the whole list of records"""

    class Meta:
        model = Position
        fields = ('id', 'url', 'title', 'active', 'time_create')


class PositionDetailSerializer(serializers.ModelSerializer):
    """Single entry data serialization class"""

    class Meta:
        model = Position
        fields = '__all__'
