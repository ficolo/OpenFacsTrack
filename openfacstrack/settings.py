"""
Django settings for openfacstrack project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "_mg%gs@@kecf==%iqwu&&-a2^_%y)na(q!vddh)5bx%5*%ycu4"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", []).split(" ")


# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "mozilla_django_oidc",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "openfacstrack.apps.track",
    "django.contrib.admin",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "mozilla_django_oidc.middleware.SessionRefresh",
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "openfacstrack.apps.track.auth.TrackOIDCAB",
)

ROOT_URLCONF = "openfacstrack.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "openfacstrack.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# OpenID configuration

OIDC_RP_SIGN_ALGO = os.environ.get("OIDC_RP_SIGN_ALGO", "RS256")
OIDC_OP_JWKS_ENDPOINT = os.environ.get(
    "OIDC_OP_JWKS_ENDPOINT",
    "http://keycloak.localhost:8080/auth/realms/openfacstrack/protocol/openid-connect/certs",
)
OIDC_RP_CLIENT_ID = os.environ.get("OIDC_RP_CLIENT_ID", "django-oidc")
OIDC_RP_CLIENT_SECRET = os.environ.get(
    "OIDC_RP_CLIENT_SECRET", "29c8b8b0-ef05-4f6a-bc98-fe6ce3ffea39"
)
OIDC_OP_AUTHORIZATION_ENDPOINT = os.environ.get(
    "OIDC_OP_AUTHORIZATION_ENDPOINT",
    "http://keycloak.localhost:8080/auth/realms/openfacstrack/protocol/openid-connect/auth",
)
OIDC_OP_TOKEN_ENDPOINT = os.environ.get(
    "OIDC_OP_TOKEN_ENDPOINT",
    "http://keycloak.localhost:8080/auth/realms/openfacstrack/protocol/openid-connect/token",
)
OIDC_OP_USER_ENDPOINT = os.environ.get(
    "OIDC_OP_USER_ENDPOINT",
    "http://keycloak.localhost:8080/auth/realms/openfacstrack/protocol/openid-connect/userinfo",
)

LOGIN_REDIRECT_URL = os.environ.get("LOGIN_REDIRECT_URL", "/track/upload/")
LOGOUT_REDIRECT_URL = os.environ.get("LOGOUT_REDIRECT_URL", "/track/")

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
