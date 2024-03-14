"""Импортирую базовый класс пагинатора"""

from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    """Мой базовый пагинатор"""

    page_size = 4  # Количество элементов на странице
    page_size_query_param = (
        "page_size"  # Параметр запроса для указания количества элементов на странице
    )
    max_page_size = 10  # Максимальное количество элементов на странице
