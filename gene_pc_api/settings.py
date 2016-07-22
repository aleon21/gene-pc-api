""" Django settings for gene_pc_api project. """

import os, sys

env = os.environ.get('ENVIRONMENT', 'dev').lower()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SECRET_KEY = os.environ.get('SECRET_KEY', None)

if env == 'dev':
    DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    'rest_framework',
    'oauth2_provider',

    "push_notifications",

    'gene_pc_api.gene_pc_api',
    'gene_pc_api.twentythreeandme',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
        'django_nose'
    ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    )
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

PUSH_NOTIFICATIONS_SETTINGS = {
    "GCM_API_KEY": os.environ.get('GCM_API_KEY', None),
    "APNS_CERTIFICATE": os.environ.get('APNS_CERTIFICATE', None),
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
            ],
        },
    },
]

WSGI_APPLICATION = 'gene_pc_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if env == 'test' or env == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME', None),
            'USER': os.environ.get('POSTGRES_USER', None),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', None),
            'HOST': os.environ.get('POSTGRES_HOST', None),
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

AUTH_USER_MODEL = 'gene_pc_api.User'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', None)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# File storage options

DATA_URL = '/data/'
DATA_STORAGE = os.path.join(BASE_DIR, "data")

TTM_RAW_URL = '/23andme/raw/'
TTM_RAW_STORAGE = os.path.join(DATA_STORAGE, '23andme', 'raw')

TTM_CONVERTED_URL = '/23andme/converted/'
TTM_CONVERTED_STORAGE = os.path.join(DATA_STORAGE, '23andme', 'converted')

CONSENT_FILE_URL = '/data/consent/'
CONSENT_FILE_LOCATION = os.path.join(DATA_STORAGE, 'consent')

# Loaded URLs

ROOT_URLCONF = 'gene_pc_api.urls'

# Sending Email

EMAIL_HOST = os.environ.get('EMAIL_HOST', None)
EMAIL_PORT = os.environ.get('EMAIL_PORT', None)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD  = os.environ.get('EMAIL_HOST_PASSWORD ', None)
EMAIL_USE_TLS = True
REGISTER_EMAIL_SUBJECT = 'Register your Account with MyGeneRank'

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django': {
            'handlers': ['file', 'console', 'mail_admins'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },

        # Send email to admins for any request errors.
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    }
}

# Celery Settings

CELERY_TASK_SERIALIZER = 'uuid_json'

try:
    BROKER_URL = os.environ['BROKER_URL']
except KeyError:
    CELERY_ALWAYS_EAGER = True
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
