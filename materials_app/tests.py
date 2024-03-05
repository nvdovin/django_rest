from rest_framework.test import APITestCase
from rest_framework import status
from user_app.models import User
from rest_framework.test import force_authenticate

# Create your tests here.

class CRUDMechanismsTest(APITestCase):
    """Тестируем CRUD механизм в приложении materials_app"""
    
    def setUp(self) -> None:
        self.user = User.objects.create(email="testcase_user@thisistest.test", password="simple_password!")
    
    def test_lessons_view(self):
        """Тест вывода списка уроков"""
        self.client.force_authenticate(self.user)
        response = self.client.get(
            path="/view_lessons/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_create(self):
        """Тест создания урока"""
        data = {
                "title": "Test lesson case",
                "description": "This is test video or lesson creating =)",
                "video_url": "https://www.youtube.com/watch?v=EXHxkwDm7c0&list=&index=2234532",
                "course": "2"
            }
        
        self.client.force_authenticate(self.user)
        response = self.client.post(
            path="/create_lesson/",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
