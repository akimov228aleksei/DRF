from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from ..models.vacation import Vacation
from ..serializers.vacation import VacationSerializer, VacationDetailSerializer


class VacationViewSet(ViewSet):
    """A class that describes all available methods with a vacation model"""

    def list(self, request):
        """The method displays all records"""
        queryset = Vacation.objects.all()
        serializer = VacationSerializer(queryset, many=True,
                                        context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """The method displays the detailed data of a particular record"""
        queryset = Vacation.objects.all()
        vacation = get_object_or_404(queryset, pk=pk)
        serializer = VacationDetailSerializer(vacation,
                                              context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """The method creates a new record"""
        serializer = VacationDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        """The method updates a specific record"""
        queryset = Vacation.objects.all()
        vacation = get_object_or_404(queryset, pk=pk)
        serializer = VacationDetailSerializer(data=request.data,
                                              instance=vacation)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """The method deletes a specific entry"""
        queryset = Vacation.objects.all()
        vacation = get_object_or_404(queryset, pk=pk)
        serializer = VacationDetailSerializer(instance=vacation)
        vacation.delete()
        return Response(serializer.data)
