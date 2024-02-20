"""Собственные, кастомные, права доступа"""
from rest_framework.permissions import BasePermission

class IsModerator(BasePermission):
    """Проверка, является ли пользователь модератором?"""

    def has_permission(self, request, view):
        """Проверка прав пользователя"""

        if request.user.is_staff:
            return True

        return view.is_moderator
        