from django.test import TestCase
from django.test import Client
from rest_framework import status
from ..models.department import Department
from django.urls import reverse
import json

from ..serializers.department import DepartmentSerializer, DepartmentDetailSerializer


class TestDepartmentViewsAPI(TestCase):

    def setUp(self):
        self.department = Department.objects.create(title='Some department_first',
                                                    description='Description about dep_first')
        self.client = Client()

    def test_get_list(self):
        response = self.client.get(reverse('department-list'))
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_detail_data(self):
        response = self.client.get(reverse('department-detail', kwargs={'pk': self.department.pk}))
        serializer = DepartmentDetailSerializer(self.department)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_data(self):
        response = self.client.get(reverse('department-detail', kwargs={'pk': None}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('department-detail', kwargs={'pk': 0}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('department-detail', kwargs={'pk': -1}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('department-detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('department-detail', kwargs={'pk': 'str'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_data(self):
        valid_data = {
            'title': 'Some department',
            'description': 'Description about some department'
        }
        response = self.client.post(reverse('department-list'),
                                    data=json.dumps(valid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 2,
                                         'title': 'Some department',
                                         'description': 'Description about some department'})

    def test_create_invalid_data(self):
        invalid_data = {
            'title': '',
            'description': ''
        }

        response = self.client.post(reverse('department-list'),
                                    data=json.dumps(invalid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_data(self):
        valid_data = {
            'title': 'Some department',
            'description': 'Description about some department'
        }
        response = self.client.put(reverse('department-detail', kwargs={'pk': self.department.pk}),
                                   data=json.dumps(valid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': self.department.pk,
                                         'title': 'Some department',
                                         'description': 'Description about some department'})

    def test_update_invalid_data(self):
        invalid_data = {
            'title': '',
            'description': ''
        }

        response = self.client.put(reverse('department-detail', kwargs={'pk': self.department.pk}),
                                   data=json.dumps(invalid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(reverse('department-detail', kwargs={'pk': None}),
                                   data=json.dumps(invalid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('department-detail', kwargs={'pk': 0}),
                                   data=json.dumps(invalid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('department-detail', kwargs={'pk': -1}),
                                   data=json.dumps(invalid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('department-detail', kwargs={'pk': 1000}),
                                   data=json.dumps(invalid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('department-detail', kwargs={'pk': 'str'}),
                                   data=json.dumps(invalid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid_data(self):
        response = self.client.delete(reverse('department-detail', kwargs={'pk': self.department.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invalid_data(self):
        response = self.client.delete(reverse('department-detail', kwargs={'pk': None}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('department-detail', kwargs={'pk': 0}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('department-detail', kwargs={'pk': -1}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('department-detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('department-detail', kwargs={'pk': 'str'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
