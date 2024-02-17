""" Импортируем модели и данного приложения и общую абстракную модель"""

from django.db import models
from django.contrib.auth.models import AbstractUser

from materials_app.models import Course, Lesson

# Create your models here.


class User(AbstractUser):
    """Собственный класс для модели пользователя"""

    username = None
    email = models.CharField(verbose_name="", unique=True)
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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payments(models.Model):
    """Модель для определения платежей пользователя"""

    user = models.CharField(verbose_name="Пользователь", max_length=200)
    payment_date = models.DateField(verbose_name="Дата оплаты")
    payed_course = models.ForeignKey(to=Course, on_delete=models.SET_NULL, null=True, blank=True)
    payed_lesson = models.ForeignKey(to=Lesson, on_delete=models.SET_NULL, null=True, blank=True)
    payment_sum = models.FloatField(verbose_name="Сумма платежа")
    payment_type = models.CharField(
        verbose_name="Тип оплаты", choices=(("CASH", "Наличные"), ("CARD", "Перевод"))
    )

    class Meta:
        """Класс для корректного отображения в админке"""
        verbose_name = "Оплата пользователя"
        verbose_name_plural = "Оплаты пользователя"
