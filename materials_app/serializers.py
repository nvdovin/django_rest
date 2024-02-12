"""Сериализаторы для удобной работы с DRF, 
а также импорт моделей, для которых будут созданы сериалхаторы"""
from rest_framework import serializers
from .models import Course, Lesson


# Создаю сериализатор для моделей


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курсов"""
    class Meta:
        """Вложенный класс для корректной работы сериализатора"""
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курсов"""
    class Meta:
        """Вложенный класс для корректной работы сериализатора"""
        model = Lesson
        fields = "__all__"
