import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lvemp9c$0svser#q!8h1_#b&tn711e6)kb^$_$totygna2)p(8'
home_path = os.path.expanduser('~')

# Estrai il nome della directory home
current_user = os.path.basename(home_path)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if current_user == 'warze' or current_user == 'user':
    DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.50']

# Application definition
import sys

PROJECT_DIR = BASE_DIR

if PROJECT_DIR.is_dir():
    APPS = [
        name for name in os.listdir(PROJECT_DIR)
        if (PROJECT_DIR / name).is_dir() and
        (PROJECT_DIR / name / 'apps.py').is_file()
    ]
else:
    APPS = []

INTERNAL_APPS = ['frontend']

INSTALLED_APPS = [
    'colorfield',
    'admin_interface',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'enhancing-boxing',
] + APPS + INTERNAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'enhancing-boxing.urls'

TEMPLATE_DIRS = [BASE_DIR / app / 'templates' for app in APPS if (BASE_DIR / app / 'templates').is_dir()]
print(f"Template_Dirs:  {TEMPLATE_DIRS}")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
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

WSGI_APPLICATION = 'enhancing-boxing.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [PROJECT_DIR / app / 'static' for app in APPS if (PROJECT_DIR / app / 'static').is_dir()] + [
    os.path.join(BASE_DIR, 'frontend'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print("MEDIA_ROOT", MEDIA_ROOT)

MAIN_STATIC_DIR = BASE_DIR / 'static'
if MAIN_STATIC_DIR.is_dir():
    STATICFILES_DIRS.append(MAIN_STATIC_DIR)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # URL del tuo frontend React
    "http://127.0.0.1:3000",
    "http://192.168.1.50",     # Aggiungi altre origini se necessario
]