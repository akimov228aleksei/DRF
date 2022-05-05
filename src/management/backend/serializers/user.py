from djoser.serializers import UserCreateSerializer
from django.db.utils import IntegrityError
from django.contrib.auth.models import Group


class UserSerializer(UserCreateSerializer):
    """A class that creates new users and adds them to the 'personal' group.
     The class overrides the serializer from the 'djoser' package"""
    def create(self, validated_data):
        try:
            group = Group.objects.get(name='personal')
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")
        except Group.DoesNotExist:
            self.fail("cannot_create_user")
        else:
            user.groups.add(group)

        return user
