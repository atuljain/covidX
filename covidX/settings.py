"""
Django settings for covidX project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import sys

from apps.apihealth.apps import APIHealthConfig

PROJECT_NAME = "covidX"
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 1800,
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "EOakcFyDvwLstAthJy1zTpSQbka1SHFm"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    os.getenv("DJANGO_ALLOWED_HOST", "localhost"),
    "127.0.0.1",
    os.getenv("DOMAIN_NAME", ""),
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "graphene_django",
    "corsheaders",
    "apps.hrm.apps.HrmConfig",
    "apps.apihealth.apps.APIHealthConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "covidX.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# WSGI_APPLICATION = "covidX.wsgi.application"

ASGI_APPLICATION = "covidX.asgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.getenv("GAE_APPLICATION", None):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "HOST": f'/cloudsql/{os.getenv("CONNECTION_NAME")}',
            "USER": f'{os.getenv("DB_USER")}',
            "PASSWORD": f'{os.getenv("DB_PWD")}',
            "NAME": f'{os.getenv("DB_NAME")}',
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "HOST": "localhost",
            "PORT": f'{os.getenv("DB_PORT", 5432)}',
            "NAME": "covid",
            "USER": "covid",
            "PASSWORD": "postgres",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # pylint: disable=line-too-long
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(os.path.join(PROJECT_ROOT, "apps/"))

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

GRAPHENE = {
    "SCHEMA": "covidX.schema.schema",
    "SCHEMA_OUTPUT": "schema.json",
    "SCHEMA_INDENT": 2,
}
