from datetime import timedelta, datetime

import pytz
from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER, TIME_ZONE
from materials.models import Course
from users.models import User


@shared_task
def sending_email_about_update(course_id):
    course = Course.objects.get(id=course_id)
    users_email_list = [subscribe.user.email for subscribe in course.subscribe.all()]
    subject = 'Новое обновление'
    message = f'Вышло обновление на курс {course.title}'
    send_mail(subject=subject,
              recipient_list=users_email_list,
              from_email=EMAIL_HOST_USER,
              message=message,
              fail_silently=True)


@shared_task
def deactivation_user_after_few_days():
    zone = pytz.timezone(TIME_ZONE)
    now_date = datetime.now()
    estimated_last_date = now_date - timedelta(days=30)
    user_list = User.objects.filter(last_login__lt=estimated_last_date, is_active=True)
    user_list.update(is_active=False)
