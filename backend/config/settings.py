from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


# ================================================================
# ENVIRONMENT HELPERS
# ================================================================

def env_bool(name, default=False):
    return os.getenv(
        name,
        str(int(default))
    ).lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


def env_list(name, default=""):
    return [
        x.strip()
        for x in os.getenv(name, default).split(",")
        if x.strip()
    ]


# ================================================================
# SECURITY
# ================================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "dev-only-change-me"
)

DEBUG = env_bool(
    "DJANGO_DEBUG",
    True
)

ALLOWED_HOSTS = env_list(
    "DJANGO_ALLOWED_HOSTS",
    "*.vercel.app,127.0.0.1,localhost"
)


# ================================================================
# APPLICATIONS
# ================================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders",
    "rest_framework",

    "company",
    "services",
    "projects",
    "quotes",
]


# ================================================================
# MIDDLEWARE
# ================================================================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ================================================================
# URL / WSGI
# ================================================================

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# ================================================================
# DATABASE
# ================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ================================================================
# INTERNATIONALIZATION
# ================================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_TZ = True


# ================================================================
# STATIC / MEDIA
# ================================================================

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"


# ================================================================
# DEFAULT MODEL FIELD
# ================================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)

APPEND_SLASH = True


# ================================================================
# CORS / CSRF
# ================================================================

CORS_ALLOWED_ORIGINS = env_list(
    "CORS_ALLOWED_ORIGINS",
    "https://issabubnigltd.vercel.app, http://127.0.0.1:5500,http://localhost:5500"
)

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https:\/\/.*\.vercel\.app$",
]

CORS_ALLOW_CREDENTIALS = True

# Allow HTTP methods used in preflight OPTIONS requests
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Allow standard request headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CSRF_TRUSTED_ORIGINS = env_list(
    "CSRF_TRUSTED_ORIGINS",
    ""
)



# ================================================================
# DJANGO REST FRAMEWORK
# ================================================================

REST_FRAMEWORK = {

    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny"
    ],

    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],

    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],

    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],

    "DEFAULT_THROTTLE_RATES": {
        "anon": "120/min",
        "user": "300/min",
        "quotes": "10/hour",
    },
}


# ================================================================
# EMAIL CONFIGURATION
# ================================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
)

EMAIL_HOST = os.getenv(
    "EMAIL_HOST",
    "smtp-mail.outlook.com"
)

EMAIL_PORT = int(
    os.getenv(
        "EMAIL_PORT",
        "587"
    )
)

EMAIL_USE_TLS = env_bool(
    "EMAIL_USE_TLS",
    True
)

EMAIL_HOST_USER = os.getenv(
    "EMAIL_HOST_USER",
    "issabubngltd@outlook.com"
)

EMAIL_HOST_PASSWORD = os.getenv(
    "EMAIL_HOST_PASSWORD",
    ""
)

DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    EMAIL_HOST_USER
)

QUOTE_NOTIFICATION_EMAIL = os.getenv(
    "QUOTE_NOTIFICATION_EMAIL",
    "issabubngltd@outlook.com"
)


# ================================================================
# PRODUCTION HARDENING
# ================================================================

if not DEBUG:

    SECURE_SSL_REDIRECT = env_bool(
        "DJANGO_SECURE_SSL_REDIRECT",
        True
    )

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"
