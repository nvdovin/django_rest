"""URLы для разнесения и облегчения проекта"""
from rest_framework.routers import DefaultRouter
from materials_app.apps import MaterialsAppConfig
from materials_app import views as v

from django.urls import path

app_name = MaterialsAppConfig.name

router = DefaultRouter()
router.register(r'course', v.CourseViewSet, basename='course')

urlpatterns = [
    path('create_lesson/', v.LessonCreateAPIView.as_view(), name='create_lesson'),
    path('view_lessons/', v.LessonListAPIView.as_view(), name='view_lessons'),
    path('view_lesson/<int:pk>/', v.LessonRetrieveAPIView.as_view(), name='view_lesson'),
    path('delete_lesson/<int:pk>/', v.LessonDestroyAPIView.as_view(), name='delete_lesson'),
    path('update_lesson/<int:pk>/', v.LessonUpdateAPIView.as_view(), name='update_lesson'),

] + router.urls
