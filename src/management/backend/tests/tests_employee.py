from django.test import TestCase
from django.test import Client
from rest_framework import status
from ..models.employee import Employee
from ..models.department import Department
from django.urls import reverse
import json
import datetime

from ..models.position import Position
from ..serializers.employee import EmployeeSerializer, EmployeeDetailSerializer


class TestEmployeeViewsAPI(TestCase):
    VALID_DATA = {
        'first_name': 'Ivan',
        'second_name': 'Ivanov',
        'birthday': '2000-01-01',
        'department': 1,
        'position': 1,
        'salary': 2000}

    VALID_DATA_UPDATE = {
        'first_name': 'Petr',
        'second_name': 'Petrov',
        'birthday': '2000-01-01',
        'department': 1,
        'position': 1,
        'salary': 1000}

    INVALID_DATA_1 = {
        'first_name': '',
        'second_name': '',
        'birthday': '',
        'department': '',
        'position': '',
        'salary': ''}

    INVALID_DATA_2 = {
        'first_name': 123,
        'second_name': 456,
        'birthday': 'some date',
        'department': 'some dep',
        'position': 'some position',
        'salary': '1000'}

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
        self.client = Client()

    def test_get_list(self):
        response = self.client.get(reverse('employee-list'))
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_detail_data(self):
        response = self.client.get(reverse('employee-detail',
                                           kwargs={'pk': self.employee.pk}))
        serializer = EmployeeDetailSerializer(self.employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_data(self):
        response = self.client.get(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_data(self):
        response = self.client.post(reverse('employee-list'),
                                    data=json.dumps(self.VALID_DATA),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 2,
                                         'first_name': 'Ivan',
                                         'second_name': 'Ivanov',
                                         'birthday': '2000-01-01',
                                         'department': self.department.pk,
                                         'position': self.position.pk,
                                         'salary': 2000,
                                         'on_boarding_day': f'{datetime.date.today()}'})

    def test_create_invalid_data(self):
        response = self.client.post(reverse('department-list'),
                                    data=json.dumps(self.INVALID_DATA_1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(reverse('department-list'),
                                    data=json.dumps(self.INVALID_DATA_2),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_data(self):
        response = self.client.put(reverse('employee-detail',
                                           kwargs={'pk': self.employee.pk}),
                                   data=json.dumps(self.VALID_DATA_UPDATE),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1,
                                         'first_name': 'Petr',
                                         'second_name': 'Petrov',
                                         'birthday': '2000-01-01',
                                         'department': self.department.pk,
                                         'position': self.position.pk,
                                         'salary': 1000,
                                         'on_boarding_day': f'{datetime.date.today()}'})

    def test_update_invalid_data_1(self):
        response = self.client.put(reverse('employee-detail',
                                           kwargs={'pk': self.employee.pk}),
                                   data=json.dumps(self.INVALID_DATA_1),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_data_2(self):
        response = self.client.put(reverse('employee-detail', kwargs={'pk': self.employee.pk}),
                                   data=json.dumps(self.INVALID_DATA_2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_data_pk_is_none(self):
        response = self.client.put(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}),
                                   data=json.dumps(self.INVALID_DATA_2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_less_than_zero(self):
        response = self.client.put(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}),
                                   data=json.dumps(self.INVALID_DATA_2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_zero(self):
        response = self.client.put(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}),
                                   data=json.dumps(self.INVALID_DATA_2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_more_than_ultimate(self):
        response = self.client.put(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}),
                                   data=json.dumps(self.INVALID_DATA_2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_string(self):
        response = self.client.put(reverse('employee-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}),
                                   data=json.dumps(self.INVALID_DATA_2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid_data(self):
        response = self.client.delete(reverse('employee-detail',
                                              kwargs={'pk': self.employee.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invalid_data_pk_is_none(self):
        response = self.client.delete(reverse('employee-detail',
                                              kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_zero(self):
        response = self.client.delete(reverse('employee-detail',
                                              kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_less_than_zero(self):
        response = self.client.delete(reverse('employee-detail',
                                              kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_more_than_ultimate(self):
        response = self.client.delete(reverse('employee-detail',
                                              kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_string(self):
        response = self.client.delete(reverse('employee-detail',
                                              kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
