"""Собственные, кастомные, права доступа"""

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка, является ли пользователь владельцем урока/курса"""

    def has_object_permission(self, request, view, obj):
        """Проверка прав пользователя на конкретный объект"""
        return request.user == obj.owner
