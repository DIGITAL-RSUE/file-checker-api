from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...services import CheckVulnerabilities
from ..serializers import FileSerializer


class FileCheckAPIView(APIView):
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        return self.check_file(request, *args, **kwargs)

    def check_file(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        messages = CheckVulnerabilities.execute(
            {
                "file_for_check": request.data["checked_file"],
            }
        )
        return Response(
            {"checked_file": messages},
            status=status.HTTP_200_OK,
        )
