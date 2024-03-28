from rest_framework.permissions import BasePermission

from materials.models import Course, Lesson
# from materials.models import Lesson, Course
from users.models import UserGroups


class IsStudentOwnerMaterial(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj in Lesson.objects.all():
            for p in request.user.payment.all():
                if p in obj.payment.all():
                    return True
                elif p in obj.course.payment.all():
                    return True
        elif obj in Course.objects.all():
            for p in request.user.payment.all():
                if p in obj.payment.all():
                    return True

class IsModerator(BasePermission):
    massage = "У вас нет прав для просмотра данной страницы"

    def has_permission(self, request, view):
        return request.user.user_groups == UserGroups.MODERATOR

