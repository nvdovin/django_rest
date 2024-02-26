"""Собственные, кастомные, права доступа"""
from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Проверка, является ли пользователь модератором?"""

    def has_permission(self, request, view):
        """Проверка прав пользователя"""
        return request.user.groups.filter(name='moderators').exists()