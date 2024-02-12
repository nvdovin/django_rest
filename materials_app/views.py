"""Импорт классов rest_framework и прочего для корректной работы приложения"""
from rest_framework import viewsets, generics

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    """Вью-сет для модели Курса"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    """CRUD механизм - создание записи """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    """CRUD механизм - просмотр записи """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """CRUD механизм - просмотр конкретной записи """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    """CRUD механизм - изменение записи """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """CRUD механизм - создание записи """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

