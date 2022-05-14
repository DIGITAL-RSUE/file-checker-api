DEFAULT_APPS = [
    "admin_interface",
    "colorfield",
    "extra_settings",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sitemaps",
    "import_export",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "drf_yasg",
    "django_cleanup.apps.CleanupConfig",
    "service_objects",
]

PROJECT_APPS = [
    "apps.core.utils",
    "apps.core.main",
    "apps.core.api",
    "apps.api.auth",
    "apps.api.file_checker",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    "django_extensions",
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
