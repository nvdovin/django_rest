"""Сериализаторы для удобной работы с DRF, 
а также импорт моделей, для которых будут созданы сериалхаторы"""
from rest_framework import serializers
from .models import Course, Lesson


# Создаю сериализатор для моделей


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курсов"""
    lessons_count = serializers.SerializerMethodField()
    lessons_is_course = serializers.SerializerMethodField()

    class Meta:
        """Вложенный класс для корректной работы сериализатора"""
        model = Course
        fields = "__all__"

    def get_lessons_count(self, instance):
        """Кастомное поле для вывода счетчика просмотров"""
        return Lesson.objects.filter(course=instance.pk).count()
    
    def get_lessons_is_course(self, instanse):
        """Кастомное поле для вывода всех уроков, которые в курсе"""
        return [[lesson.title, lesson.description] for lesson in Lesson.objects.filter(course=instanse.pk)]


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курсов"""

    class Meta:
        """Вложенный класс для корректной работы сериализатора"""
        model = Lesson
        fields = "__all__"
