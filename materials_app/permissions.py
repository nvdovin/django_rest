"""Собственные, кастомные, права доступа"""
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка, является ли пользователь владельцем урока/курса"""

    def has_object_permission(self, request, view, obj):
        """Проверка прав пользователя на конкретный объект"""
        # Без превращения в strig формат сравнение не проходит. Нашел такой выход.
        return str(request.user) == str(obj.owner)
    