from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from study.models import Course, Lesson
from study.serializers import CourseSerializer, LessonSerializer
from study.permissions import IsModerator, IsStudentAllowViewLessonOrCourse


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'list':
            self.permission_classes = [IsModerator]
        elif self.action == 'retrieve':
            self.permission_classes = [IsModerator | IsStudentAllowViewLessonOrCourse]
        elif self.action == 'update':
            self.permission_classes = [IsModerator | IsStudentAllowViewLessonOrCourse]
        elif self.action == 'destroy':
            self.permission_classes = [IsStudentAllowViewLessonOrCourse]

        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsStudentAllowViewLessonOrCourse]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsStudentAllowViewLessonOrCourse]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsStudentAllowViewLessonOrCourse]
