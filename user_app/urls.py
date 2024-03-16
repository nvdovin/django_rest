"""Вынес urls этого приложения в отдельный файл"""

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path
from user_app.apps import UserAppConfig
from user_app import views as v

# Название этого приложения
app_name = UserAppConfig.name


urlpatterns = [
    # Приложение ures_app
    path("payments/", v.PaymentsAPIListView.as_view(), name="payments_listview"),
    path("users_list/", v.UserAPIListView.as_view(), name="users_list"),
    path("create_user/", v.UserCreateAPIView.as_view(), name="create_user"),
    path("update_user/<int:pk>/", v.UserUpdateAPIView.as_view(), name="update_user"),
    path("del_user/<int:pk>/", v.UserDeleteAPIView.as_view(), name="del_user"),
    # djangorestframework-simplejwt
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Оплата продукции для урока 5
    path("pay/", v.PaymentMakeAPICreateView.as_view(), name="pay_for_product"),

]
