"""
Django settings for fiveup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path

# Parse database configuration from $DATABASE_URL
import dj_database_url

from django.core.exceptions import ImproperlyConfigured

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fuauth",
    "messagebox",
    "messagevault",
    "widget_tweaks",
    "parsley",
    "courier",
    "email_log",
    "django_extensions",
)

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "fiveup.urls"

WSGI_APPLICATION = "fiveup.wsgi.application"


# overridden by dj-database-url
DATABASES = {}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Los_Angeles"

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "fuauth.User"

LOGIN_REDIRECT_URL = "/login/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = "staticfiles"

STATIC_URL = "/static/"

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static"
    # Always use forward slashes
    # Don't forget to use absolutel paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "messagebox/templates"),
            os.path.join(BASE_DIR, "fuauth/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


EMAIL_BACKEND = "email_log.backends.EmailBackend"
EMAIL_LOG_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = get_env_variable("SENDGRID_API_KEY")
DEFAULT_FROM_EMAIL = "Five Up <app44043297@heroku.com>"

WSGI_APPLICATION = "fiveup.wsgi.application"


DATABASES["default"] = dj_database_url.config(
    default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Allow all host headers
ALLOWED_HOSTS = ["*"]


sentry_sdk.init(
    dsn="https://1dc4252ef5c54824ac5cb9b5ec9fe9b7@sentry.io/5178781",
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
