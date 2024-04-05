from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from materials.permissions import IsModerator, IsStudentOwnerMaterial
from users.models import SubscribeToUpdate
from users.serializers import SubscribeToUpdateSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'list':
            self.permission_classes = [IsModerator]
        elif self.action == 'retrieve':
            self.permission_classes = [IsModerator | IsStudentOwnerMaterial]
        elif self.action == 'update':
            self.permission_classes = [IsModerator | IsStudentOwnerMaterial]
        elif self.action == 'destroy':
            self.permission_classes = [IsStudentOwnerMaterial]

        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser | IsStudentOwnerMaterial]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsStudentOwnerMaterial]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsStudentOwnerMaterial]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsStudentOwnerMaterial]


class SubscribeToUpdateAPIView(generics.UpdateAPIView):
    """активирует подписку авторизованного пользователя к выбранному, передаваемому, курсу"""
    serializer_class = SubscribeToUpdateSerializer
    queryset = Course.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        print(self.request.data)

        course = self.request.data.get('course')
        print(course)
        course_item = get_object_or_404(Course, id=course)
        # Метод get_or_create() возвращает объект,
        # а если его нет в бд, то добавляет в бд новый объект.
        subs_item = SubscribeToUpdate.objects.get_or_create(user=user, course=course_item)

        if subs_item[0].is_active:
            subs_item[0].is_active = False
            message = 'Подписка удалена'
            subs_item[0].save()

        else:
            subs_item[0].is_active = True
            message = 'Подписка добавлена'
            subs_item[0].save()

        return Response(message)
