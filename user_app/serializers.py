"""Файл для описания сериализаторов приложения user_app"""
from rest_framework import serializers

from user_app.models import Payments


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для приложения user_app, для модели Платежей"""

    class Meta:
        """Вложенный класс для настройки вышестоящего класса"""
        model = Payments
        fields = "__all__"
