from django.core.validators import FileExtensionValidator
from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    checked_file = serializers.FileField(
        write_only=True,
        validators=[
            FileExtensionValidator(
                (
                    "xls",
                    "xlm",
                    "xlsx",
                    "xlsm",
                    "doc",
                    "docx",
                    "docm",
                    "ppt",
                    "pps",
                    "pptx",
                    "ppsx",
                    "ppam",
                    "odt",
                    "odp",
                    "ods",
                    "pptm",
                    "pdf",
                    "rtf",
                )
            )
        ],
    )

    class Meta:
        fields = ("checked_file",)

    def is_valid(self, raise_exception=False):
        if not hasattr(self, "_validated_data"):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except serializers.ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            raise serializers.ValidationError(self.errors)

        return not bool(self._errors)
