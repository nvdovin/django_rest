"""Импорт классов rest_framework и прочего для корректной работы приложения"""

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from materials_app.paginators import MyPagination
from .permissions import IsOwner
from user_app.permissions import IsModerator

from .models import Course, Lesson, CourseSubscribe
from .serializers import CourseSerializer, LessonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    """Вью-сет для модели Курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = []
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [IsAdminUser(), ]
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
    pagination_class = MyPagination

    def get(self, request):
        """Насколько я понимаю, это замена метода родительского класса"""
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

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


class SubscriptionAPIView(APIView):
    """Механизм для смены флага подписки на курс"""

    def post(self, request, *args, **kwargs):
        """Реализация задания через post метод"""
        user = request.user  
        course_id = request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = CourseSubscribe.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            CourseSubscribe.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'

        return Response({"message": message}, status=status.HTTP_200_OK)
