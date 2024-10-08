"""
Django settings for the project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "dummy secret")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "True").lower() in ["true", "1", "on"]


ALLOWED_HOSTS = [host.strip() for host in os.environ.get("ALLOWED_HOSTS", "").split(",")]

DEFAULT_ALLOWED_ORIGINS = ["http://0.0.0.0", "http://localhost:3000"]
CORS_ALLOWED_ORIGINS = [
    origin.strip() for origin in os.environ.get("ALLOWED_ORIGINS", "").split(",") if origin
] or DEFAULT_ALLOWED_ORIGINS


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api",
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

ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "api.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST", "dummy_DB_HOST"),
        "PORT": os.environ.get("DB_PORT", "dummy_DB_PORT"),
        "USER": os.environ.get("DB_USER", "dummy_DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "dummy_DB_PASSWORD"),
        "NAME": os.environ.get("DB_NAME", "dummy_DB_NAME"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOG_FORMAT_MODE = os.environ.get("LOG_FORMAT_MODE", "text" if DEBUG else "json")
LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    # ...
    "formatters": {
        "text": {
            # For running locally (Docker, debugger), use whatever format you like (modify this string).
            "format": "{asctime} [{process}/{thread}] {levelname} ({name}@{module}): {message}",
            "style": "{",
            "class": "common.utils.ExtraFormatter",
        },
        "json": {
            # List of fields, not actually a format.
            "format": "%(asctime) %(thread) %(process) %(levelname) %(name) %(module) %(message)",
            "class": "common.utils.CustomJsonFormatter",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": LOG_FORMAT_MODE,
        },
        "console_custom": {
            "level": os.environ.get("LOG_LEVEL", "DEBUG"),
            "class": "logging.StreamHandler",
            "formatter": LOG_FORMAT_MODE,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "home": {
            "handlers": ["console_custom"],
            "level": "DEBUG",
            "propagate": False,
        },
        "gunicorn.error": {
            "handlers": ["console"],
            "propagate": False,
        },
        # Fine-tune some spamming loggers.
        "django.utils.autoreload": {
            "level": "INFO",
        },
        "django.server": {
            "level": "WARNING",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}


DEFAULT_SUPERUSER_PASSWORD = os.environ.get("DEFAULT_SUPERUSER_PASSWORD")
DEFAULT_SUPERUSER_NAME = os.environ.get("DEFAULT_SUPERUSER_NAME", "admin_default")
DEFAULT_SUPERUSER_EMAIL = os.environ.get("DEFAULT_SUPERUSER_EMAIL", "admin_default@main.com")
