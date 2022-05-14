"""Rest framework settings"""
from datetime import timedelta

from config.settings.base import env

DATE_INPUT_FORMATS = [
    ("%d-%m-%Y"),
    ("%d.%m.%Y"),
    ("%d/%m/%Y"),
    "iso-8601",
]


REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": (
    # ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "DATE_FORMAT": "%d/%m/%Y",
    "DATE_INPUT_FORMATS": DATE_INPUT_FORMATS,
    "DATETIME_FORMAT": "%d/%m/%Y %H:%M",
}

CORS_ALLOW_CREDENTIALS = True

REST_USE_JWT = True
JWT_AUTH_COOKIE = "access_token"


# JWT_AUTH_SECURE = not env("DEBUG", default=True)
# JWT_AUTH_HTTPONLY = True
# JWT_AUTH_SAMESITE = "Lax"
# OLD_PASSWORD_FIELD_ENABLED = True
# LOGOUT_ON_PASSWORD_CHANGE = True

CORS_ALLOW_ALL_ORIGINS = True

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "apps.api.auth.v1.serializers.UserDetailsSerializer",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=365),
}
