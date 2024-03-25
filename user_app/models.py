""" Импортируем модели и данного приложения и общую абстракную модель"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """Собственный класс для модели пользователя"""

    username = None
    email = models.EmailField(verbose_name="email", unique=True, max_length=100)
    avatar = models.ImageField(
        verbose_name="Аватарка", upload_to="media/users", blank=True, null=True
    )
    birthday = models.DateTimeField(
        verbose_name="Дата рождения", null=True, blank=True, default=None
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона", max_length=12, blank=True, null=True
    )
    city = models.CharField(verbose_name="Город", max_length=50, blank=True, null=True)
    temporary_password = models.CharField(
        verbose_name="Temporary password", max_length=6, blank=True, null=True
    )
    is_moderator = models.BooleanField(verbose_name="Модератор?", default=False)
    last_login = models.DateTimeField(verbose_name="Последнее посещение сервиса", auto_now=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
