from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from ..models.employee import Position
from ..serializers.position import PositionSerializer


class PositionViewSet(ViewSet):

    def list(self, request):
        queryset = Position.objects.all()
        serializer = PositionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Position.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = PositionSerializer(department)
        return Response(serializer.data)

    def create(self, request):
        serializer = PositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Position.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = PositionSerializer(data=request.data, instance=department)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Position.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = PositionSerializer(instance=department)
        department.delete()
        return Response(serializer.data)
