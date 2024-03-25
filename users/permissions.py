from rest_framework.permissions import BasePermission

from users.models import UserGroups


class IsStudentReadList(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_groups == UserGroups.STUDENT:
            return True
        return False


class IsStudentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False
