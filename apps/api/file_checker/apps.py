from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FileCheckerConfig(AppConfig):
    """Default app config"""

    name = "apps.api.file_checker"
    verbose_name = _("FileChecker")
