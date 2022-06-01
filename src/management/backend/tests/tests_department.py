from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.db.models import Q

from datetime import date
import json

from ..models.department import Department
from ..serializers.department import DepartmentSerializer, DepartmentDetailSerializer


class TestDepartmentViewsAPI(APITestCase):
    VALID_DATA = {
        'title': 'Some department',
        'description': 'Description about some department'
    }

    INVALID_DATA = {
        'title': '',
        'description': ''
    }

    VALID_DATA_UPDATE = {
        'title': 'Some updated department',
        'description': 'Description about some updated department'
    }

    INVALID_PK_STRING = 'str'

    INVALID_PK_LESS_THAN_ZERO = -1

    INVALID_PK_MORE_THAN_ULTIMATE = 1000

    INVALID_PK_ZERO = 0

    INVALID_PK_NONE = None

    def setUp(self):
        self.department = Department.objects.create(title='Some department_first',
                                                    description='Description about dep_first')
        user = User.objects.create_user(username='Alex', password='1q2w3e')
        self.client.force_authenticate(user=user)
        permissions = Permission.objects.filter(Q(codename='add_department') |
                                                Q(codename='change_department') |
                                                Q(codename='delete_department'))
        user.user_permissions.add(*permissions)

    def test_get_list(self):
        response = self.client.get(reverse('department-list'))
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True,
                                          context={'request': response.wsgi_request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_detail_data(self):
        response = self.client.get(reverse('department-detail',
                                           kwargs={'pk': self.department.pk}))
        serializer = DepartmentDetailSerializer(self.department)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_data_pk_is_none(self):
        response = self.client.get(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_zero(self):
        response = self.client.get(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_less_than_zero(self):
        response = self.client.get(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_more_than_ultimate(self):
        response = self.client.get(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_string(self):
        response = self.client.get(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_data(self):
        response = self.client.post(reverse('department-list'),
                                    data=json.dumps(self.VALID_DATA),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'url': f"http://testserver{reverse('department-detail', kwargs={'pk': 2})}",
                                         'id': 2,
                                         'title': 'Some department',
                                         'description': 'Description about some department',
                                         'time_create': f'{date.today()}',
                                         'time_update': response.data['time_update']})

    def test_create_invalid_data(self):
        response = self.client.post(reverse('department-list'),
                                    data=json.dumps(self.INVALID_DATA),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_data(self):
        response = self.client.put(reverse('department-detail',
                                           kwargs={'pk': self.department.pk}),
                                   data=json.dumps(self.VALID_DATA_UPDATE),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'url': f"http://testserver{reverse('department-detail', kwargs={'pk': 1})}",
                                         'id': 1,
                                         'title': 'Some updated department',
                                         'description': 'Description about some updated department',
                                         'time_create': f'{date.today()}',
                                         'time_update': response.data['time_update']})

    def test_update_invalid_data(self):
        response = self.client.put(reverse('department-detail',
                                           kwargs={'pk': self.department.pk}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_data_pk_is_none(self):
        response = self.client.put(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_zero(self):
        response = self.client.put(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_less_than_zero(self):
        response = self.client.put(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_more_than_zero(self):
        response = self.client.put(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_string(self):
        response = self.client.put(reverse('department-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid_data(self):
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.department.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invalid_data_pk_is_none(self):
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_zero(self):
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_less_than_zero(self):
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_more_than_zero(self):
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_string(self):
        response = self.client.delete(reverse('department-detail',
                                              kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
