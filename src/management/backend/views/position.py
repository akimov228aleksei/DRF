from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from ..models.employee import Position
from ..serializers.position import PositionSerializer


class PositionViewSet(ViewSet):
    """A class that describes all available methods with a position model"""

    def list(self, request):
        """The method displays all records"""
        queryset = Position.objects.all()
        serializer = PositionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """The method displays the detailed data of a particular record"""
        queryset = Position.objects.all()
        position = get_object_or_404(queryset, pk=pk)
        serializer = PositionSerializer(position)
        return Response(serializer.data)

    def create(self, request):
        """The method creates a new record"""
        serializer = PositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        """The method updates a specific record"""
        queryset = Position.objects.all()
        position = get_object_or_404(queryset, pk=pk)
        serializer = PositionSerializer(data=request.data, instance=position)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """The method deletes a specific entry"""
        queryset = Position.objects.all()
        position = get_object_or_404(queryset, pk=pk)
        serializer = PositionSerializer(instance=position)
        position.delete()
        return Response(serializer.data)
