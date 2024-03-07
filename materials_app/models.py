"""Импортируем родительский класс для создания модели"""

from django.db import models

from config import settings

# Create your models here.


class Course(models.Model):
    """Модель для описания курсов на проекте"""

    title = models.CharField(verbose_name="Название курса", max_length=255, unique=True)
    preview = models.ImageField(verbose_name="Превью курса", blank=True, null=True)
    description = models.TextField(verbose_name="Описание курса")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        "Вложенный класс для отображения в админке"
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель для создания и описания уроков внутри курса"""

    title = models.CharField(verbose_name="Название урока", max_length=255, unique=True)
    description = models.TextField(verbose_name="Описание урока")
    preview = models.ImageField(verbose_name="Превью урока", blank=True, null=True)
    video_url = models.URLField(max_length=200, unique=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        """Вложенный класс для описания уроков в адмике"""

        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class CourseSubscribe(models.Model):
    """Подписка / отписка
    Модель, призвана к реазиции подписки или отписки на курс"""

    course = models.ForeignKey(
        to="Course",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Курс",
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Пользователь",
    )

    class Meta:
        """Вложенный класс для описания подписки в адмике"""

        verbose_name = "Пописка"
        verbose_name_plural = "Пописки"
