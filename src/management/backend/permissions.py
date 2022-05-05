from rest_framework import permissions


class IsAdminOrManagerOrReadOnly(permissions.BasePermission):
    """A class that checks users permissions to modify models"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == 'create':
            return request.user.has_perm(f'backend.add_{view.basename}')

        if view.action == 'update':
            return request.user.has_perm(f'backend.change_{view.basename}')

        if view.action == 'destroy':
            return request.user.has_perm(f'backend.delete_{view.basename}')
