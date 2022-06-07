from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet

from ..models.position import Position
from ..serializers.position import PositionSerializer, PositionDetailSerializer


class PositionViewSet(ViewSet):
    """A class that describes all available methods with a position model"""

    def get_queryset(self):
        """The method that generates the queryset"""
        queryset = Position.objects.all()
        # If query parameter 'active' == True -> show only active records
        if eval(self.request.query_params.get('active', 'False')):
            queryset = Position.objects.filter(active=True)
        return queryset

    def list(self, request):
        """The method displays all records"""
        queryset = self.get_queryset()
        serializer = PositionSerializer(queryset, many=True,
                                        context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """The method displays the detailed data of a particular record"""
        queryset = self.get_queryset()
        position = get_object_or_404(queryset, pk=pk)
        serializer = PositionDetailSerializer(position,
                                              context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """The method creates a new record"""
        serializer = PositionDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        """The method updates a specific record"""
        queryset = self.get_queryset()
        position = get_object_or_404(queryset, pk=pk)
        serializer = PositionDetailSerializer(data=request.data,
                                              instance=position)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """The method deletes a specific entry"""
        queryset = self.get_queryset()
        position = get_object_or_404(queryset, pk=pk)
        serializer = PositionDetailSerializer(instance=position)
        position.delete()
        return Response(serializer.data)
