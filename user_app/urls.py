"""Вынес urls этого приложения в отдельный файл"""
from django.urls import path
from user_app.apps import UserAppConfig
from user_app import views as v

# Название этого приложения
app_name = UserAppConfig.name


urlpatterns = [
    path("payments/", v.UserAPIListView.as_view(), name="payments_listview"),

]
