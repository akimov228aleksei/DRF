from rest_framework.generics import get_object_or_404
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet
from ..models.department import Department
from ..serializers.department import DepartmentSerializer, DepartmentDetailSerializer


class DepartmentViewSet(ViewSet):

    def list(self, request):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentDetailSerializer(department)
        return Response(serializer.data)

    def create(self, request):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentSerializer(data=request.data, instance=department)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentSerializer(instance=department)
        department.delete()
        return Response(serializer.data)


# class DepartmentView(APIView):
#
#     def get(self, request, **kwargs):
#         if kwargs.get('pk', None):
#             pk = kwargs['pk']
#             try:
#                 response = Department.objects.get(pk=pk)
#             except:
#                 return Response({'error': 'Object does not exists'})
#
#             response = DepartmentDetailSerializer(response).data
#             return Response({'post': response})
#
#         response = Department.objects.all()
#         return Response({'posts': DepartmentSerializer(response, many=True).data})
#
#     def post(self, request):
#         response = DepartmentSerializer(data=request.data)
#         response.is_valid(raise_exception=True)
#         response.save()
#         return Response({'post_added': response.validated_data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Department.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         response = DepartmentSerializer(data=request.data, instance=instance)
#         response.is_valid(raise_exception=True)
#         response.save()
#         return Response({'post_updated': response.data})
#
#     def delete(self, request, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#
#         try:
#             instance = Department.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Objects does not exists'})
#
#         response = DepartmentSerializer(instance).data
#         instance.delete()
#         return Response({'deleted': response})