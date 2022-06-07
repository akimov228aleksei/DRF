from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.db.models import Q

import json

from ..models.department import Department
from ..models.employee import Employee
from ..models.position import Position
from ..models.vacation import Vacation
from ..serializers.vacation import VacationSerializer, VacationDetailSerializer


class TestVacationViewsAPI(APITestCase):
    VALID_DATA = {
        'employee': 2,
        'start_date': '2022-07-01',
        'end_date': '2022-07-23'
    }

    INVALID_DATA = {
        'employee': '',
        'start_date': '',
        'end_date': ''
    }

    VALID_DATA_UPDATE = {
        'employee': 1,
        'start_date': '2022-05-02',
        'end_date': '2022-05-25'
    }

    INVALID_PK_STRING = 'str'

    INVALID_PK_LESS_THAN_ZERO = -1

    INVALID_PK_MORE_THAN_ULTIMATE = 1000

    INVALID_PK_ZERO = 0

    INVALID_PK_NONE = None

    def setUp(self):
        self.department = Department.objects.create(title='Some department_first',
                                                    description='Description about dep_first')
        self.position = Position.objects.create(title='Some position',
                                                max_salary=4000)
        self.employee = Employee.objects.create(first_name='Ivan',
                                                second_name='Ivanov',
                                                birthday='2000-02-20',
                                                department=self.department,
                                                position=self.position,
                                                salary=2000)
        self.employee_2 = Employee.objects.create(first_name='Petr',
                                                  second_name='Petrov',
                                                  birthday='2010-03-03',
                                                  department=self.department,
                                                  position=self.position,
                                                  salary=3000)
        self.vacation = Vacation.objects.create(employee=self.employee,
                                                start_date='2022-02-02',
                                                end_date='2022-03-03')
        user = User.objects.create_user(username='Alex', password='1q2w3e')
        self.client.force_authenticate(user=user)
        permissions = Permission.objects.filter(Q(codename='add_vacation') |
                                                Q(codename='change_vacation') |
                                                Q(codename='delete_vacation'))
        user.user_permissions.add(*permissions)

    def test_get_list(self):
        response = self.client.get(reverse('vacation-list'))
        vacation = Vacation.objects.all()
        serializer = VacationSerializer(vacation, many=True,
                                        context={'request': response.wsgi_request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_detail_data(self):
        response = self.client.get(reverse('vacation-detail',
                                           kwargs={'pk': self.vacation.pk}))
        serializer = VacationDetailSerializer(self.vacation)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_data_pk_is_none(self):
        response = self.client.get(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_zero(self):
        response = self.client.get(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_less_than_zero(self):
        response = self.client.get(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_more_than_ultimate(self):
        response = self.client.get(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_string(self):
        response = self.client.get(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_data(self):
        response = self.client.post(reverse('vacation-list'),
                                    data=json.dumps(self.VALID_DATA),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 2,
                                         'employee_first_name': self.employee_2.first_name,
                                         'employee_second_name': self.employee_2.second_name,
                                         'employee': self.employee_2.pk,
                                         'start_date': '2022-07-01',
                                         'end_date': '2022-07-23'})

    def test_create_invalid_data(self):
        response = self.client.post(reverse('vacation-list'),
                                    data=json.dumps(self.INVALID_DATA),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_data(self):
        response = self.client.put(reverse('vacation-detail',
                                           kwargs={'pk': self.vacation.pk}),
                                   data=json.dumps(self.VALID_DATA_UPDATE),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1,
                                         'employee_first_name': self.employee.first_name,
                                         'employee_second_name': self.employee.second_name,
                                         'employee': self.employee.pk,
                                         'start_date': '2022-05-02',
                                         'end_date': '2022-05-25'})

    def test_update_invalid_data(self):
        response = self.client.put(reverse('vacation-detail',
                                           kwargs={'pk': self.vacation.pk}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_data_pk_is_none(self):
        response = self.client.put(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_less_than_zero(self):
        response = self.client.put(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_zero(self):
        response = self.client.put(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_more_than_ultimate(self):
        response = self.client.put(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_string(self):
        response = self.client.put(reverse('vacation-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid_data(self):
        response = self.client.delete(reverse('vacation-detail',
                                              kwargs={'pk': self.vacation.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invalid_data_pk_is_none(self):
        response = self.client.delete(reverse('vacation-detail',
                                              kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_zero(self):
        response = self.client.delete(reverse('vacation-detail',
                                              kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_less_than_zero(self):
        response = self.client.delete(reverse('vacation-detail',
                                              kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_more_than_ultimate(self):
        response = self.client.delete(reverse('vacation-detail',
                                              kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_string(self):
        response = self.client.delete(reverse('vacation-detail',
                                              kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)