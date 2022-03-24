from rest_framework.views import APIView, Response
from ..models.department import Department
from ..serializers.department import DepartmentSerializer, DepartmentDetailSerializer


class DepartmentView(APIView):

    def get(self, request, **kwargs):
        if kwargs.get('pk', None):
            pk = kwargs['pk']
            try:
                response = Department.objects.get(pk=pk)
            except:
                return Response({'error': 'Object does not exists'})

            response = DepartmentDetailSerializer(response).data
            return Response({'post': response})

        response = Department.objects.all()
        return Response({'posts': DepartmentSerializer(response, many=True).data})

    def post(self, request):
        response = DepartmentSerializer(data=request.data)
        response.is_valid(raise_exception=True)
        response.save()
        return Response({'post_added': response.validated_data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Department.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        response = DepartmentSerializer(data=request.data, instance=instance)
        response.is_valid(raise_exception=True)
        response.save()
        return Response({'post_updated': response.data})

    def delete(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Department.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        response = DepartmentSerializer(instance).data
        instance.delete()
        return Response({'deleted': response})