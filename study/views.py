from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from study.models import Course, Lesson
from study.serializers import CourseSerializer, LessonSerializer
from study.permissions import IsModerator, IsStaff, IsStudentAllowViewLessonOrCourse


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsStaff]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsModerator]
        elif self.action == 'retrieve':
            self.permission_classes = [IsModerator | IsStudentAllowViewLessonOrCourse]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsStaff]

        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsStaff]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsStaff]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsStudentAllowViewLessonOrCourse]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]
