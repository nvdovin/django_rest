"""Импорт классов rest_framework и прочего для корректной работы приложения"""

from rest_framework import viewsets, generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from config import settings
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
    
    def get_queryset(self):
        qs = Course.objects.all()
        if not self.request.user.is_moderator:
            qs = qs.owner(self.request.user)
        return qs


class LessonCreateAPIView(generics.CreateAPIView):
    """CRUD механизм - создание записи"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    """CRUD механизм - просмотр записи"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


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
