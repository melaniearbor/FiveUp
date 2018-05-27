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

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fuauth',
    'messagebox',
    'messagevault',
    'widget_tweaks',
    'django_modalview',
    'parsley',
    'courier',
    'email_log',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fiveup.urls'

WSGI_APPLICATION = 'fiveup.wsgi.application'


# overridden by dj-database-url
DATABASES = {

}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'fuauth.User'

LOGIN_REDIRECT_URL = '/login/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    #Put strings here, like "/home/html/static"
    #Always use forward slashes
    #Don't forget to use absolutel paths, not relative paths.
    os.path.join(
        BASE_DIR,
        'static',
    ),
)

TEMPLATE_DIRS = (
    os.path.join(
        BASE_DIR,
        'messagebox/templates',
    ),
    os.path.join(
        BASE_DIR,
        'fuauth/templates',
    ),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
)

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'email_log.backends.EmailBackend'
EMAIL_LOG_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = get_env_variable("SENDGRID_API_KEY")
DEFAULT_FROM_EMAIL = "Five Up <app44043297@heroku.com>"

WSGI_APPLICATION = 'fiveup.wsgi.application'

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config(default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3"))

print(DATABASES['default'])

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
