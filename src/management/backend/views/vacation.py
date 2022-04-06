from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from ..models.vacation import Vacation
from ..serializers.vacation import VacationSerializer


class VacationViewSet(ViewSet):

    def list(self, request):
        queryset = Vacation.objects.all()
        serializer = VacationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Vacation.objects.all()
        vacation = get_object_or_404(queryset, pk=pk)
        serializer = VacationSerializer(vacation)
        return Response(serializer.data)

    def create(self, request):
        serializer = VacationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Vacation.objects.all()
        vacation = get_object_or_404(queryset, pk=pk)
        serializer = VacationSerializer(data=request.data, instance=vacation)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Vacation.objects.all()
        vacation = get_object_or_404(queryset, pk=pk)
        serializer = VacationSerializer(instance=vacation)
        vacation.delete()
        return Response(serializer.data)
