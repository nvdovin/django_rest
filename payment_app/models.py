from django.db import models

from materials_app.models import Course, Lesson
from user_app.models import User

# Create your models here.

class Payments(models.Model):
    """Модель для определения платежей пользователя"""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)
    payed_course = models.ForeignKey(
        to=Course, on_delete=models.CASCADE, null=True, blank=True
    )
    payed_lesson = models.ForeignKey(
        to=Lesson, on_delete=models.CASCADE, null=True, blank=True
    )
    payment_sum = models.FloatField(verbose_name="Сумма платежа", default=1000)
    payment_type = models.CharField(
        verbose_name="Тип оплаты",
        choices=(("CASH", "Наличные"), ("CARD", "Перевод")),
        max_length=5,
        default="CASH"
    )
    payment_url = models.TextField(blank=True, null=True, verbose_name="URL оплаты")
    session_id = models.CharField(max_length=255, verbose_name="ID сессии", blank=True, null=True)

    class Meta:
        """Класс для корректного отображения в админке"""

        verbose_name = "Оплата пользователя"
        verbose_name_plural = "Оплаты пользователя"
