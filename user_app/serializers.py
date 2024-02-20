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
    password = serializers.CharField(write_only=True)

    class Meta:
        """Вложенный класс для настройки модели сериализатора"""
        model = User
        fields = "__all__"

    def create(self, validated_data):
        """Метод для хеширования сырого пароля"""

        password = validated_data.pop("password")       # Получаем и удаляем сырой пароль
        user = User(**validated_data)                   # Ролучаем экземпляр текущего пользователя
        user.set_password(password)                     # Устанавливаем хешированный пароль
        user.save()                                     # Мохраняем пользователя с новым паролем
        return user
