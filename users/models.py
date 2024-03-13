from django.contrib.auth.models import AbstractUser
from django.db import models

from study.models import Course, Lesson

NULLABLE: dict[str, bool] = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='имя')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):

    PAYMENT_METHOD = [
        ('CASH', 'наличные'),
        ('NON_CASH', 'перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment')
    date_pay = models.DateField(verbose_name='дата оплаты')
    amount_payment = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method_payment = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name='метод оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payment', verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payment', verbose_name='оплаченный урок', **NULLABLE)
