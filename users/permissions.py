from rest_framework.permissions import BasePermission

from users.models import UserGroups


class IsMember(BasePermission):
    massage = "У вас нет прав для просмотра данной страницы"

    def has_permission(self, request, view):
        return request.user.user_groups == UserGroups.MEMBER


class IsMemberOwnerProfile(BasePermission):
    massage = "У вас нет прав для просмотра данной страницы"

    def has_object_permission(self, request, view, obj):
        return request.user == obj
