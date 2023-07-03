import os
from pathlib import Path

from moviepagol.config import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == 'True'

ALLOWED_HOSTS = ["*"]

# Application definition
DEFAULT_APPS = [
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "app_main",
    "api",
]
THRIRDPARTY_APPS = [
    # 'admin_volt.apps.AdminVoltConfig',
    "django_summernote",
    "nested_admin",
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THRIRDPARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "moviepagol.urls"

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
                "django.template.context_processors.request",
                "app_main.custom_contextprocessor.servemodels",
                "app_main.custom_contextprocessor.site",
            ],
        },
    },
]

WSGI_APPLICATION = "moviepagol.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "db.sqlite3"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_URL = "/static/"
MEDIA_URL = "/mediafiles/"

# Media files
if not DEBUG:
    MEDIA_ROOT = ROOT / DOMAIN_ROOT / "mediafiles"
    STATIC_ROOT = ROOT / DOMAIN_ROOT / "static"
else:
    MEDIA_ROOT = BASE_DIR / "mediafiles"
    STATIC_ROOT = BASE_DIR / "staticfiles"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django jet theme
JET_THEMES = [
    {
        "theme": "default",  # theme folder name
        "color": "#47bac1",  # color of the theme's button in user menu
        "title": "Default",  # theme title
    },
    {"theme": "green", "color": "#44b78b", "title": "Green"},
    {"theme": "light-green", "color": "#2faa60", "title": "Light Green"},
    {"theme": "light-violet", "color": "#a464c4", "title": "Light Violet"},
    {"theme": "light-blue", "color": "#5EADDE", "title": "Light Blue"},
    {"theme": "light-gray", "color": "#222", "title": "Light Gray"},
]

JET_SIDE_MENU_ITEMS = [
    {
        "label": ("Series"),
        "items": [
            {"name": "app_main.seriesmodel", "label": ("Series")},
            {"name": "app_main.seasonmodel", "label": ("Seasons")},
            {"name": "app_main.episodemodel", "label": ("Episodes")},
        ],
    },
    {
        "label": ("Movies"),
        "items": [
            {"name": "app_main.moviemodel", "label": ("Movies")},
            {"name": "app_main.bsubmodel", "label": ("BSub")},
            {"name": "app_main.classicmodel", "label": ("Classic")},
            {"name": "app_main.satyajitraymodel", "label": ("Satyajit Ray")},
            {"name": "app_main.jamesbondmodel", "label": ("James Bond 007")},
            {"name": "app_main.dualaudiomodel", "label": ("Dual Audio")},
            {"name": "app_main.hindidubbedmodel", "label": ("Hindi Dubbed")},
            {"name": "app_main.imdbtopmodel", "label": ("IMDB Top")},
            {"name": "app_main.oscarwinningmodel", "label": ("Oscar Winning")},
            {"name": "app_main.superheromodel", "label": ("Superhero")},
            {"name": "app_main.footagemodel", "label": ("Found Footage")},
        ],
    },
    {
        "label": ("Softwares, Games and Apps"),
        "items": [
            {
                "name": "app_main.softwaresgamesmodel",
                "label": ("Softwares,Games,Apps,Extras"),
            },
        ],
    },
    {
        "label": ("Top-Slide and Special"),
        "items": [
            {"name": "app_main.topslidemodel", "label": ("Top-Slide")},
            {"name": "app_main.specialmodel", "label": ("Special")},
        ],
    },
    {
        "label": ("Extra"),
        "items": [
            {"name": "app_main.genremodel", "label": ("Genres")},
            {"name": "app_main.bsubcreatormodel", "label": ("BSub Translator")},
            {"name": "app_main.notice", "label": ("Notices")},
        ],
    },
    {
        "label": ("user account and groups"),
        "items": [
            {"name": "auth.user"},
            {"name": "auth.group"},
        ],
    },
]

JET_SIDE_MENU_COMPACT = True
X_FRAME_OPTIONS = "SAMEORIGIN"
