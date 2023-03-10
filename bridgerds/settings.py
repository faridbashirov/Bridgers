"""
Django settings for bridgerds project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

DEBUG = int(os.environ.get("DEBUG", default=1))
PROD = not DEBUG
SECRET_KEY = os.environ.get("SECRET_KEY", "&*lc95ge)ooukh-jvf$ad&h9w64rpp4@s_)ar_dk9o%*ej63h)")
ALLOWED_HOSTS = ['*'] # os.environ.get("ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',

    # Third party apps
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    'django.contrib.sitemaps',
    'rest_framework',
]

# GOOGLE_RECAPTCHA_SITE_KEY = '6Lcoo0ckAAAAAM8I6Xl-fiEVIlHDwjH-M4woxOr5'
# GOOGLE_RECAPTCHA_SECRET_KEY = '6Lcoo0ckAAAAAIqLuMxSveJROHXtuNLjXaZIPOHB'

# RECAPTCHA_REQUIRED_SCORE = 0.85
# SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bridgerds.urls'

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
                'core.context_processor.service_renderer'
            ],
        },
    },
]

WSGI_APPLICATION = 'bridgerds.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Leman',
#         'USER': 'postgres',
#         'PASSWORD': 'leman123',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'db_name'),
        'USER': os.environ.get('POSTGRES_USER', 'user_name'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432),
        'HOST': os.environ.get('POSTGRES_HOST', '5.161.121.186'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '123')
    }
}

# ckeditor configurations

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format', 'Styles'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'ImageButton', 'Source']
        ]
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

if PROD:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
    
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}

RECAPTCHA_PUBLIC_KEY = '6Lf7rmckAAAAANCXOkgqhZVL4zU-2He8zW35iqkt'
RECAPTCHA_PRIVATE_KEY = '6Lf7rmckAAAAAFOi3f5puPXn9JAQ_wJm0MxJoalr'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# RECAPTCHA_PUBLIC_KEY  = '6LcVJGckAAAAABMXOc0K3IX-V2PrV_0Gmwv7A5us'
# RECAPTCHA_PRIVATE_KEY = '6LcVJGckAAAAAJuUUt4kDVZcvyb0BsK3yhP7mBSF'
# SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# RECAPTCHA_REQUIRED_SCORE = 0.85



import ssl
ssl._create_default_https_context = ssl._create_unverified_context
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER ='g.heyderov@gmail.com'
# EMAIL_HOST_PASSWORD = 'ebcrdibkujskwrvp'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='office@bridgerds.com'
EMAIL_HOST_PASSWORD = 'gtpxriqszcgsvhzy'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CSRF_TRUSTED_ORIGINS=['https://*.bridgerds.com', 'https://bridgerds.com']
