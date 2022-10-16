import os

from badi_utils.email import Email
from badi_utils.sms import IpPanelSms
from badi_utils.validations import PersianValidations, BadiValidators

from .project_config import *
from django.utils.translation import ugettext_lazy as _, gettext_noop
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = SECRET_KEY
DEBUG_MODE_ACTIVE = os.getenv('DEBUG_MODE_ACTIVE')
USE_SQLITE = os.getenv('USE_SQLITE')
if DEBUG_MODE_ACTIVE == "1":
    DEBUG = True
else:
    DEBUG = False
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'badi_user',
    'badi_ticket',
    'badi_wallet',
    'badi_utils',
    'rest_framework',
    'widget_tweaks',
    'django_filters',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
REST_FRAMEWORK = REST_FRAMEWORK
ROOT_URLCONF = PROJECT_DIRECTORY + '.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = PROJECT_DIRECTORY + '.wsgi.application'

if USE_SQLITE == '1':
    DATABASES = DEFAULT_DATABASE_SQLITE
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQL_NAME', 'db_' + PROJECT_DIRECTORY),
            'USER': os.getenv('MYSQL_USER', 'root'),
            'PASSWORD': os.getenv('MYSQL_PASS', '4542'),
            'HOST': os.getenv('MYSQL_HOST', 'localhost'),
            'PORT': os.getenv('MYSQL_PORT', '3306'),
        }
    }
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]
AUTH_USER_MODEL = 'badi_user.User'
LOG_MODEL = 'badi_user.Log'
LOGIN_REDIRECT_URL = gettext_noop('/')
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
LANGUAGE_CODE = 'fa-IR'
LANGUAGES = (
    ('fa', _('Persian')),
)
TIME_ZONE = 'Asia/Tehran'
expects_localtime = True
USE_I18N = True
USE_L10N = True
USE_TZ = False
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TIME_INPUT_FORMATS = [
    '%H:%M',  # '14:30',
]
JWT_AUTH = JWT_AUTH

BADI_AUTH_CONFIG = {
    "resend": {
        "is_active": True,
        "class": IpPanelSms,
        "user_find_key": "username",
        "token_key": "phone",
        "user_key": "mobile_number",
        "errors": {
            "404": _("No active user found")
        }
    },
    "verify": {
        "is_active": True,
        "user_find_key": "username",
        "token_key": "phone",
        "user_key": "mobile_number",
    },
    "register": {
        "is_active": True,
        "user_find_key": "username",
        "token_key": "phone",
        "user_key": "mobile_number",
        "email_active": False,
        "mobile_number_active": True,
        "mobile_number_validator": PersianValidations.phone_number,
        "email_panel": PersianValidations.phone_number,
        "sms_panel": IpPanelSms,
        "username_validator": BadiValidators.username,
    },
    "login": {
        "is_active": True,
        "type": "username_password",
        "auto_create": True,
        "login_to_django": True,
        "user_key": "username",
        "email_panel": Email.send_login_token,
        "sms_panel": IpPanelSms,
        "username_validator": PersianValidations.phone_number,
    },
    "sms": {
        "is_active": True,
        "sms_panel": IpPanelSms,
    },
}
