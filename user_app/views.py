"""Пока что пустой файл для того, чтобы в будущем наполнить его DRF штучками"""
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from user_app.models import Payments
from user_app.serializers import PaymentSerializer

class UserAPIListView(generics.ListAPIView):
    """Для того, чтобы показать все данные о пользователе"""
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("payed_course", "payed_lesson", "payment_type")
    ordering_fields = ("payment_date", )
