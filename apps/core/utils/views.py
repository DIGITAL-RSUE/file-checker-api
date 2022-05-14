import io

import xlsxwriter
from django.http import HttpResponse
from django.views import View
from num2words import num2words
from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    IntegerField,
    Serializer,
    SerializerMethodField,
)
from rest_framework.views import APIView


def num2words_filter(number):
    """
    Функция обертка для создания фильтра jinja2
    которая преобразует числов в его текстовое представление
    на русском языке
    """
    return num2words(number, lang="ru")


class XLSXView(View):
    """
    Базовый класс представления для генерации .xlsx документа.

    Подробнее: [xlsxwriter](https://xlsxwriter.readthedocs.io/)
    """

    file_name = "file"

    def get(self, request, *args, **kwargs):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        self.create_file(
            self.get_context_data(**kwargs),
            workbook,
            worksheet,
            **kwargs,
        )

        workbook.close()
        output.seek(0)

        file_name = self.get_file_name(**kwargs)
        response = HttpResponse(
            output,
            content_type=(
                "application/vnd.openxmlformats"
                "-officedocument.spreadsheetml.sheet"
            ),
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{file_name}.xlsx"'

        return response

    def get_file_name(self, **kwargs):
        return self.file_name

    def get_context_data(self, **kwargs):
        return {}

    def create_file(self, context, workbook, worksheet, **kwargs):
        pass


class BaseChoiceView(APIView):
    """
    Базовый класс представления API
    для получения списка choices
    """

    objects = None

    class ChoiceSerializer(Serializer):
        """Сериализатор для ModelChoice"""

        id = IntegerField(read_only=True)
        name = CharField(read_only=True, max_length=100)
        short_name = SerializerMethodField()

        def get_short_name(self, obj):
            return obj["name"][0]

    def choice_to_dict(self, items):
        """Метод преобразовывает ModelChoice в dict"""
        for el in items:
            yield {"id": el[0], "name": el[1]}

    def get(self, request):
        objetcs = list(self.choice_to_dict(self.objects))
        serializer = self.ChoiceSerializer(objetcs, many=True)
        return Response(serializer.data)
