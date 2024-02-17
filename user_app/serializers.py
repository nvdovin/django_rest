"""Файл для описания сериализаторов приложения user_app"""
from rest_framework import serializers

from user_app.models import Payments, User


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для приложения user_app, для модели Платежей"""

    class Meta:
        """Вложенный класс для настройки вышестоящего класса"""
        model = Payments
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Пользователей"""

    class Meta:
        """Вложенный класс для настройки модели сериализатора"""
        model = User
        fields = "__all__"
