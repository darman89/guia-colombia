from rest_framework import permissions


class IsTheUserOrCreate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST' or request.method == 'PATCH':
            return True
        elif obj is not None and request.user.is_authenticated():
            return obj.id == request.user.id
        else:
            return False
