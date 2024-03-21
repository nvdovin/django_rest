"""Вынес urls этого приложения в отдельный файл"""


from django.urls import path
from payment_app import views
from payment_app.apps import PaymentAppConfig

# Название этого приложения
app_name = PaymentAppConfig.name

urlpatterns = [
    path("pay/", views.PaymentAPIView.as_view(), name="payment"),
]
