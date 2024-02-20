"""Импортируем родительский класс для создания модели"""

from django.db import models

# Create your models here.


class Course(models.Model):
    """Модель для описания курсов на проекте"""

    title = models.CharField(verbose_name="Название курса", max_length=255, unique=True)
    preview = models.ImageField(verbose_name="Превью курса", blank=True, null=True)
    description = models.TextField(verbose_name="Описание курса")
    owner = models.CharField(verbose_name="Владелец", default=None, blank=True, null=True)

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
    owner = models.CharField(verbose_name="Владелец", default=None, blank=True, null=True)

    class Meta:
        """Вложенный класс для описания уроков в адмике"""

        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
