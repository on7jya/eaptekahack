import os
from pathlib import Path

from celery.schedules import crontab
from environs import Env

env = Env()
env.read_env(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=sxrwu%7m$z!=*($(b)cke8d*0iqi#l=_qmps+u)&5j^^v62r5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


AUTH_USER_MODEL = 'eaptekahack.User'

# Application definition


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': [],
}


INSTALLED_APPS = [
    'drf_yasg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'config',
    'eaptekahack',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASS'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
        'CONN_MAX_AGE': 600,
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# STATIC
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"

# MINIO
MINIO_STORAGE_ENDPOINT = env.str('MINIO_STORAGE_ENDPOINT')
MINIO_STORAGE_ACCESS_KEY = env.str('MINIO_ACCESS_KEY')
MINIO_STORAGE_SECRET_KEY = env.str('MINIO_SECRET_KEY')
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'local-media'
MINIO_STORAGE_MEDIA_URL = f'{env.str("MINIO_STORAGE_URL")}/{MINIO_STORAGE_MEDIA_BUCKET_NAME}'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True

MINIO_STORAGE_STATIC_BUCKET_NAME = 'local-static'
MINIO_STORAGE_STATIC_URL = f'{env.str("MINIO_STORAGE_URL")}/{MINIO_STORAGE_STATIC_BUCKET_NAME}'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True

# CELERY
CELERY_BROKER_URL = env.str('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env.str('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TIMEZONE = "UTC"
CELERY_WORKER_POOL_RESTARTS = "True"


CELERY_BEAT_SCHEDULE = {
    'generate_event': {'task': 'config.tasks.generate_event_for_push', 'schedule': crontab(minute=1),},
}
