from rest_framework.permissions import BasePermission

from study.models import Lesson, Course
from users.models import UserGroups


class IsStudentAllowViewLessonOrCourse(BasePermission):
    """
    Проверяет проплачен ли курс/урок у пользователя.
    Если проплачен урок - return True на данный урок
    Если проплачен курс - return True на данный курс и на уроки в данном курсе
    Иначе return False
    """

    massage = "У вас нет прав для просмотра данной страницы"
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
        else:
            return False


class IsModerator(BasePermission):
    massage = "У вас нет прав для просмотра данной страницы"

    def has_permission(self, request, view):
        if request.user.user_groups == UserGroups.MODERATOR:
            return True
        return False

class IsStaff(BasePermission):
    massage = "У вас нет прав для просмотра данной страницы"
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
