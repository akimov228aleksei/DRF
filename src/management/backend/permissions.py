from rest_framework import permissions


class IsAdminOrManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print(view.action)
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == 'create':
            return request.user.has_perm(f'backend.add_{view.basename}')

        if view.action == 'update':
            return request.user.has_perm(f'backend.update_{view.basename}')

        if view.action == 'delete':
            return request.user.has_perm(f'backend.delete_{view.basename}')