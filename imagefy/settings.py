"""
Django settings for Imagefy project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse as db_url

ADMINS = (
    ('André Luiz', 'contato@xdvl.info'),
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).absolute().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'collectfast',
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # rest_framework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_auth',
    'rest_auth.registration',
    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    # 3rd
    'debug_toolbar',
    'django_extensions',
    'storages',
    'corsheaders',
    'mptt',
    # Project
    'imagefy.core',
    'imagefy.wishes',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'imagefy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR / 'imagefy' / 'templates'),
        ],
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

WSGI_APPLICATION = 'imagefy.wsgi.application'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'imagefy.core.middleware.show_toolbar'
}


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {'default': config('DATABASE_URL', cast=db_url)}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# AWS
# https://boto3.readthedocs.org/en/latest/

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', '123')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', '456')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', 'imagefy')

AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN', 's3.amazonaws.com/imagefy')

AWS_PRELOAD_METADATA = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')
DEFAULT_S3_PATH = 'media'

STATICFILES_STORAGE = config('STATICFILES_STORAGE', 'django.contrib.staticfiles.storage.StaticFilesStorage')
STATIC_S3_PATH = 'static'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    str(BASE_DIR / 'imagefy' / 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR / 'media-root')

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR / 'static-root')

# E-mail
# https://docs.djangoproject.com/en/1.9/topics/email/

EMAIL_SUBJECT_PREFIX = '[Imagefy] '

# Auth
# https://docs.djangoproject.com/en/1.9/topics/auth

LOGIN_REDIRECT_URL = '/'

# Django-Allauth
# http://django-allauth.readthedocs.io/en/stable/configuration.html

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': [
            'email',
        ],
        'AUTH_PARAMS': {
            'auth_type': 'reauthenticate',
        },
        'FIELDS': [
            'id',
            'email',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.6',
    },
}

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_USERNAME_REQUIRED = False

SOCIALACCOUNT_EMAIL_VERIFICATION = False

# Logging
# https://docs.djangoproject.com/en/1.9/topics/logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Testing
# https://model-mommy.readthedocs.io/en/latest/index.html

MOMMY_CUSTOM_FIELDS_GEN = {
    'autoslug.fields.AutoSlugField': 'model_mommy.generators.gen_text',
}


# CORS
# https://github.com/ottoyiu/django-cors-headers

CORS_ORIGIN_ALLOW_ALL = True


# rest_framework
# http://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

# Shopify
# https://help.shopify.com/api/reference

SHOPIFY_BUY_CLIENT_SHOP = "imagefy.myshopify.com"
SHOPIFY_BUY_CLIENT_API_KEY = "2f1f599bd8ba116edf14399407e99e19"
SHOPIFY_BUY_CLIENT_CHANNEL = "55729859"
