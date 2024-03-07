"""Импорт нужного для реализации задачи готового участка рест фреймворка"""

from rest_framework import serializers


class YoutubeValidator:
    """### Youtube Serialiser
    Описываю свой валидатор для проверки того, не приложил ли полльзователть какую-то ссылку,
    кроме как на ютуб
    """

    def __init__(self, field) -> None:
        self.field = field

    def __call__(self, value):
        temp_value = dict(value).get(self.field)
        if "youtube.com" not in temp_value:
            raise serializers.ValidationError("Это не ссылка на youtube")
