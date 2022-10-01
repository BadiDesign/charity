import os
from datetime import timedelta
from rest_framework.reverse import reverse_lazy

LOGIN_URL = reverse_lazy('custom_login')
PROJECT_NAME = 'خباد'
CONFIG_JSON = {
    'site_title': PROJECT_NAME,
    'title': "خباد | موسسه خیریخ حمایت از بیماران بادرود ",
    'description': 'خباد | موسسه خیریخ حمایت از بیماران بادرود - آدرس: اصفهان بادرود، سه راه مرکز شهر',
    'keywords': 'موسسه،خیریه،حمایت',
    'author': 'بادی دیزاین',

}
DEFAULT_DATABASE_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
PROJECT_DIRECTORY = 'charity'
SECRET_KEY = os.getenv("SECRET_KEY")
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=90),
}
DISABLE_FORM_SUBMIT = True  # غیر فعال کردن Dynamic های بدون Api
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': timedelta(days=90),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=90),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_LOGIN_URLS ': LOGIN_URL,
    'JWT_AUTH_COOKIE': None,
}
