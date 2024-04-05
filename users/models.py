from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _tr

from materials.models import Course, Lesson


NULLABLE: dict[str, bool] = {'blank': True, 'null': True}


class UserGroups(models.TextChoices):

    MEMBER = 'Member', _tr('Member')
    MODERATOR = 'Moderator', _tr('Moderator')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=False)
    user_groups = models.CharField(verbose_name='группа пользователя',
                                   choices=UserGroups.choices,
                                   max_length=10, default='Member')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.user_groups}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk',)


class Payment(models.Model):

    PAYMENT_METHOD = [
        ('CASH', 'наличные'),
        ('NON_CASH', 'перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment')
    date_pay = models.DateField(verbose_name='дата оплаты')
    amount_payment = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method_payment = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name='метод оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='payment',
                               verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name='payment',
                               verbose_name='оплаченный урок', **NULLABLE)

    def __str__(self):
        return f'Дата: {self.date_pay},' \
               f'Сумма: {self.amount_payment},' \
               f'Метод оплаты: {self.method_payment},' \
               f'За {self.course if self.course else self.lesson}.'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('-date_pay',)


class SubscribeToUpdate(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', related_name='subscribe', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='курс', related_name='subscribe', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name='подписка на обновление')

    def __str__(self):
        return (f'Пользователь: {self.user.first_name} {self.user.last_name}'
                f'{self.course.title}'
                f'Активна: {self.is_active}')

    class Meta:
        verbose_name = 'подписка на обновление'
        verbose_name_plural = 'подписки на обновление'
