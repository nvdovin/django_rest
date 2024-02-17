"""Вынес urls этого приложения в отдельный файл"""
from django.urls import path
from user_app.apps import UserAppConfig
from user_app import views as v

# Название этого приложения
app_name = UserAppConfig.name


urlpatterns = [
    path("payments/", v.PaymentsAPIListView.as_view(), name="payments_listview"),
    path("users_list/", v.UserAPIListView.as_view(), name="users_list"),
    path("create_user/", v.UserCreateAPIView.as_view(), name="create_user"),
    
]
