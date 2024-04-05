from django.urls import path

from materials.apps import StudyConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscribeToUpdateAPIView

app_name = StudyConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='courses-create'),
                  path('lesson/', LessonListAPIView.as_view(), name='courses-list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='courses-get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='courses-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='courses-delete'),

                  path('course/subscribe/', SubscribeToUpdateAPIView.as_view(), name='subscribe'),

              ] + router.urls
