"""Импорт классов rest_framework и прочего для корректной работы приложения"""

from rest_framework import viewsets, generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from config.permissions import IsModerator

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
    permission_classes = [IsModerator]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """CRUD механизм - изменение записи"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """CRUD механизм - создание записи"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
