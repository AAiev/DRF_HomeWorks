from django.contrib.auth.models import AbstractUser
from django.db import models

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
