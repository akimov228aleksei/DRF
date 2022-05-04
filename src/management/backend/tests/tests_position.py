from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.db.models import Q

import json
import datetime

from ..models.position import Position
from ..serializers.position import PositionSerializer, PositionDetailSerializer


class TestPositionViewsAPI(APITestCase):
    VALID_DATA = {
        'title': 'Position number 1',
        'max_salary': 500
    }

    INVALID_DATA = {
        'title': '',
        'max_salary': ''
    }

    VALID_DATA_UPDATE = {
        'title': 'Updated position number 1',
        'max_salary': 3000
    }

    INVALID_PK_STRING = 'str'

    INVALID_PK_LESS_THAN_ZERO = -1

    INVALID_PK_MORE_THAN_ULTIMATE = 1000

    INVALID_PK_ZERO = 0

    INVALID_PK_NONE = None

    def setUp(self):
        self.position = Position.objects.create(title='Some position',
                                                max_salary=4000)
        user = User.objects.create_user(username='Alex', password='1q2w3e')
        self.client.force_authenticate(user=user)
        permissions = Permission.objects.filter(Q(codename='add_position') |
                                                Q(codename='change_position') |
                                                Q(codename='delete_position'))
        user.user_permissions.add(*permissions)

    def test_get_list(self):
        response = self.client.get(reverse('position-list'))
        position = Position.objects.all()
        serializer = PositionSerializer(position, many=True,
                                        context={'request': response.wsgi_request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_detail_data(self):
        response = self.client.get(reverse('position-detail',
                                           kwargs={'pk': self.position.pk}))
        serializer = PositionDetailSerializer(self.position)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_data_pk_is_none(self):
        response = self.client.get(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_zero(self):
        response = self.client.get(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_less_than_zero(self):
        response = self.client.get(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_more_than_ultimate(self):
        response = self.client.get(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_detail_data_pk_is_string(self):
        response = self.client.get(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_data(self):
        response = self.client.post(reverse('position-list'),
                                    data=json.dumps(self.VALID_DATA),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 2,
                                         'title': 'Position number 1',
                                         'max_salary': 500,
                                         'active': True,
                                         'time_create': f'{datetime.date.today()}'})

    def test_create_invalid_data(self):
        response = self.client.post(reverse('position-list'),
                                    data=json.dumps(self.INVALID_DATA),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_data(self):
        response = self.client.put(reverse('position-detail',
                                           kwargs={'pk': self.position.pk}),
                                   data=json.dumps(self.VALID_DATA_UPDATE),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1,
                                         'title': 'Updated position number 1',
                                         'active': True,
                                         'max_salary': 3000,
                                         'time_create': f'{datetime.date.today()}'})

    def test_update_invalid_data(self):
        response = self.client.put(reverse('position-detail',
                                           kwargs={'pk': self.position.pk}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_data_pk_is_none(self):
        response = self.client.put(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_NONE}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_less_than_zero(self):
        response = self.client.put(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_zero(self):
        response = self.client.put(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_ZERO}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_more_than_ultimate(self):
        response = self.client.put(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid_data_pk_is_string(self):
        response = self.client.put(reverse('position-detail',
                                           kwargs={'pk': self.INVALID_PK_STRING}),
                                   data=json.dumps(self.INVALID_DATA),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid_data(self):
        response = self.client.delete(reverse('position-detail',
                                              kwargs={'pk': self.position.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invalid_data_pk_is_none(self):
        response = self.client.delete(reverse('position-detail',
                                              kwargs={'pk': self.INVALID_PK_NONE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_zero(self):
        response = self.client.delete(reverse('position-detail',
                                              kwargs={'pk': self.INVALID_PK_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_less_than_zero(self):
        response = self.client.delete(reverse('position-detail',
                                              kwargs={'pk': self.INVALID_PK_LESS_THAN_ZERO}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_more_than_ultimate(self):
        response = self.client.delete(reverse('position-detail',
                                              kwargs={'pk': self.INVALID_PK_MORE_THAN_ULTIMATE}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_data_pk_is_string(self):
        response = self.client.delete(reverse('position-detail',
                                              kwargs={'pk': self.INVALID_PK_STRING}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
