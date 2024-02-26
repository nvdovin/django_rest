"""Импорт классов rest_framework и прочего для корректной работы приложения"""

from rest_framework import viewsets, generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner
from user_app.permissions import IsModerator

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    """Вью-сет для модели Курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [IsAdminUser()]
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    """CRUD механизм - создание записи"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    """CRUD механизм - просмотр записи"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """CRUD механизм - просмотр конкретной записи"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsOwner]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """CRUD механизм - изменение записи"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsOwner]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """CRUD механизм - создание записи"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser, IsOwner]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
