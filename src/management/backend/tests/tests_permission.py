from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.db.models import Q

from ..models.department import Department
from ..serializers.department import DepartmentSerializer


class TestDepartmentViewsAPI(APITestCase):

    def setUp(self):
        self.department_1 = Department.objects.create(title='Some department_first',
                                                      description='Description about dep_first')
        self.department_2 = Department.objects.create(title='Some department_second',
                                                      description='Description about dep_second')
        self.user = User.objects.create_user(username='Alex', password='1q2w3e')
        self.user_token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        permissions = Permission.objects.filter(Q(codename='add_department') |
                                                Q(codename='change_department') |
                                                Q(codename='delete_department'))
        self.user.user_permissions.add(*permissions)

    def test_get_list_with_permissions(self):
        response = self.client.get(reverse('department-list'))
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True,
                                          context={'request': response.wsgi_request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_with_permissions(self):
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.department_1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_without_token(self):
        self.client.credentials()
        response = self.client.get(reverse('department-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_without_token(self):
        self.client.credentials()
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.department_2.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_without_permissions(self):
        permission_delete = Permission.objects.get(codename='delete_department')
        self.user.user_permissions.remove(permission_delete)
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.department_2.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
