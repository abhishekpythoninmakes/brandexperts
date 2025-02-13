"""
Django settings for BrandExpertsEcommerce project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t7*2el()8a*qrz%!p#quy8m-%6rlgb(7m@#xk*!(tk+m95#dk9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'dash.brandexperts.ae',
    'www.brandexperts.ae',
    'brandexperts.ae',
    'localhost',
    '127.0.0.1',
    'http://localhost:5173',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'corsheaders',
    'django.contrib.contenttypes',
    'whitenoise.runserver_nostatic',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'customer',
    'products_app',
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BrandExpertsEcommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'BrandExpertsEcommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MYBE',
        'USER': 'admin',
        'PASSWORD': 'database1brandexperts',
        'HOST':'databasebe.cz6qg420mik4.ap-south-1.rds.amazonaws.com',
        'PORT':3306
    }
}


AUTH_USER_MODEL = 'products_app.CustomUser'


CORS_ALLOWED_ORIGINS = [
    "https://brandexperts.ae",
    "http://localhost:5173",
    "https://www.brandexperts.ae",
    "https://dash.brandexperts.ae",
]



CORS_ALLOW_CREDENTIALS = True


CSRF_TRUSTED_ORIGINS = [
    "https://brandexperts.ae",
    "https://api.brandexperts.ae",
    "https://dash.brandexperts.ae",
    "https://www.brandexperts.ae",
    "http://localhost:5173",
]



CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
    "accept",
    "origin",
    "x-requested-with",
    "x-csrftoken"
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
import os

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Your email service provider's SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hiddenhope00@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'dmkgmnwhnnbbglfu'  # Your email password
DEFAULT_FROM_EMAIL = 'hiddenhope00@gmail.com'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'extraPlugins': ','.join([
            'justify', 'autogrow', 'clipboard', 'dialog', 'div', 'find', 'font', 'image', 'link',
            'liststyle', 'pagebreak', 'pastetext', 'preview', 'table', 'templates','uploadimage','image2',
        ]),
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserBrowseUrl': '/ckeditor/browse/',
    },
}

CKEDITOR_UPLOAD_PATH = "uploads/"

