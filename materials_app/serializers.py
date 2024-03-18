"""Сериализаторы для удобной работы с DRF, 
а также импорт моделей, для которых будут созданы сериалхаторы"""

from rest_framework import serializers
import stripe

from config import settings
from materials_app.validators import YoutubeValidator
from .models import Course, Lesson


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
        user = self.context["request"].user
        lesson = Lesson(**validated_data)
        lesson.owner = user
        lesson.save()
        return lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курсов"""

    lessons_count = serializers.SerializerMethodField()
    lessons_in_course = LessonSerializer(many=True, read_only=True, source="lesson_set")
    payment_url = serializers.SerializerMethodField()

    class Meta:
        """Вложенный класс для корректной работы сериализатора"""

        model = Course
        fields = "__all__"

    def get_lessons_count(self, instance):
        """Кастомное поле для вывода счетчика просмотров"""
        return Lesson.objects.filter(course=instance.pk).count()
    
    def get_payment_url(self, obj):
        """Метод для создания сессии покупки, как учили нас наши наставники"""
        stripe.api_key = settings.STRIPE_SECRET_KEY  # Указываем секретный ключ Stripe

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': obj.title,
                    },
                    'unit_amount': 30000,  # Цена в копейках
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'http://localhost:8000/view_lesson/{obj.id}/',  # URL после успешной оплаты
            cancel_url='https://example.com/view_lessons/',    # URL в случае отмены оплаты
        )
        return session.url

    def create(self, validated_data):
        """Автоматическое добавление пользователя в новосоданный экземпляр класса"""
        user = self.context["request"].user
        print(user)
        course = Course(**validated_data)
        course.owner = user
        course.save()
        return course
