"""Пока что пустой файл для того, чтобы в будущем наполнить его DRF штучками"""
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsModerator

from user_app.models import Payments, User
from user_app.serializers import PaymentSerializer, UserSerializer

class PaymentsAPIListView(generics.ListAPIView):
    """Для того, чтобы показать все данные о пользователе"""
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("payed_course", "payed_lesson", "payment_type")
    ordering_fields = ("payment_date", )


class UserAPIListView(generics.ListAPIView):
    """Просмотр всех пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Изменение пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsModerator]


class UserDeleteAPIView(generics.DestroyAPIView):
    """Удаление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsModerator]
