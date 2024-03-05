"""Сериализаторы для удобной работы с DRF, 
а также импорт моделей, для которых будут созданы сериалхаторы"""
from rest_framework import serializers

from materials_app.validators import YoutubeValidator
from .models import Course, Lesson, CourseSubscribe


# Создаю сериализатор для моделей
class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курсов"""

    class Meta:
        """Вложенный класс для корректной работы сериализатора"""
        model = Lesson
        fields = "__all__"
        validators = [YoutubeValidator(field="video_url")]

    def create(self, validated_data):
        """Автоматическое добавление пользователя в новосоданный экземпляр класса"""
        user = self.context['request'].user
        lesson = Lesson(**validated_data)
        lesson.owner = user
        lesson.save()
        return lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курсов"""
    lessons_count = serializers.SerializerMethodField()
    lessons_in_course = LessonSerializer(many=True, read_only=True, source="lesson_set")

    class Meta:
        """Вложенный класс для корректной работы сериализатора"""
        model = Course
        fields = "__all__"

    def get_lessons_count(self, instance):
        """Кастомное поле для вывода счетчика просмотров"""
        return Lesson.objects.filter(course=instance.pk).count()

    def create(self, validated_data):
        """Автоматическое добавление пользователя в новосоданный экземпляр класса"""
        user = self.context['request'].user
        print(user)
        course = Course(**validated_data)
        course.owner = user
        course.save()
        return course
