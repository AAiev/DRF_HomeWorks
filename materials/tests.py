from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Lesson, Course
from users.models import User, SubscribeToUpdate


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.test', password='123', first_name='FNAME', last_name='LNAME')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='TEST_course',
            description='TEST_course_description'
        )
        self.lesson = Lesson.objects.create(
            title='TEST_lesson',
            description='TEST_lesson_description',
            course=self.course,
            url_video='https://www.youtube.com/test123'
        )
        self.subscribe = SubscribeToUpdate.objects.create(
            user=self.user,
            course=self.course
        )

    def test_create_course(self):
        """тестирование создания курса"""
        data = {
            'title': 'TEST_course',
            'description': 'TEST_course_description'
        }
        response = self.client.post('/course/',
                                    data=data
                                    )
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED
                         )

        self.assertEqual(response.json(),
                         {
                             'id': response.json()['id'], 'title': 'TEST_course',
                             'description': 'TEST_course_description',
                             'image_preview': None, 'quantity_lessons': 0,
                             'lesson': []
                         }
                         )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_course_list(self):
        """Тестирование вывода списка курсов"""
        response = self.client.get(
            '/course/'
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {'count': 1, 'next': None, 'previous': None, 'results': [
                             {'id': self.course.id, 'title': 'TEST_course', 'description': 'TEST_course_description',
                              'image_preview': None, 'quantity_lessons': 1,
                              'lesson': [{'id': self.lesson.id, 'url_video': 'https://www.youtube.com/test123',
                                          'title': 'TEST_lesson', 'description': 'TEST_lesson_description',
                                          'image': None, 'course': self.course.id}]}]})

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_lesson_list(self):
        """Тестирование вывода экземпляра курса"""

        response = self.client.get(
            reverse('materials:lesson-list'),
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {'count': 1, 'next': None, 'previous': None, 'results': [
                             {'id': self.lesson.id, 'url_video': 'https://www.youtube.com/test123',
                              'title': 'TEST_lesson',
                              'description': 'TEST_lesson_description', 'image': None, 'course': self.course.id}]}
                         )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_lesson_retrieve(self):
        """Тестирование вывода экземпляра курса"""

        response = self.client.get(
            reverse('materials:lesson-get', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {'id': self.lesson.pk, 'url_video': 'https://www.youtube.com/test123', 'title': 'TEST_lesson',
                          'description': 'TEST_lesson_description',
                          'image': None, 'course': self.lesson.course.pk}
                         )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_lesson_create(self):
        """тестирование создания урока"""
        data = {
            'title': 'TEST_lesson',
            'description': 'TEST_lesson_description',
            'course': self.course.id,
            'url_video': 'https://www.youtube.com/test123'
        }
        response = self.client.post(
            reverse('materials:lesson-create', ),
            data=data
        )

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED
                         )

        self.assertEqual(response.json(),
                         {'id': response.json()['id'], 'url_video': 'https://www.youtube.com/test123',
                          'title': 'TEST_lesson',
                          'description': 'TEST_lesson_description', 'image': None, 'course': self.course.id}
                         )
        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_lesson_update(self):
        """Тестирование обновление экземпляра урока"""

        data = {
            'title': 'TEST_lesson123',
            'description': 'TEST_lesson_description123',
            'url_video': 'https://www.youtube.com/test'
        }
        response = self.client.patch(
            reverse('materials:lesson-update', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {'id': self.lesson.pk, 'url_video': 'https://www.youtube.com/test', 'title': 'TEST_lesson123',
                          'description': 'TEST_lesson_description123',
                          'image': None, 'course': self.lesson.course.pk}
                         )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_lesson_validator_url(self):
        data = {
            'title': 'TEST_lesson',
            'description': 'TEST_lesson_description',
            'course': self.course.id,
            'url_video': 'https://www.mail.mail'
        }
        response = self.client.post(
            reverse('materials:lesson-create', ),
            data=data
        )

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {'url_video': ['Некорректный адрес']}
        )

    def test_subscribe(self):
        data = {
            'user': self.user.id,
            'course': self.course.id
        }

        response = self.client.post(
            reverse('materials:subscribe'),
            data=data
        )

        print(response.json())

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        self.assertTrue(response.json(), 'True')
