"""
Django's settings for AkachaRestaurant project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# import dj_database_url
<<<<<<< Updated upstream
import environ

import cloudinary
import cloudinary.uploader
import cloudinary.api

env = environ.Env()
=======
# import environ

# env = environ.Env()
>>>>>>> Stashed changes

# environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "wertgfdioamsdnfndkgiof"
# SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
    'hotelmanagement',
    'StockManagerApp',
    'EmployeeManagement',

    # 'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AkachaRestaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hotelmanagement.processor.user_type_list',
                'hotelmanagement.processor.message_analyser',
            ],
        },
    },
]

WSGI_APPLICATION = 'AkachaRestaurant.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     "default": dj_database_url.parse(env("DATABASE_URL"))
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }

# Set session timeout to 5 minutes (in seconds)
# SESSION_COOKIE_AGE = 300
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

<<<<<<< Updated upstream
# adding config
cloudinary.config(
  cloud_name = "dvbdol5uj",
  api_key = "463778388412657",
  api_secret = "-ohofO2WCM2YdwCgbGfocwCsGNs"
)


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

=======
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

>>>>>>> Stashed changes
# STATIC_ROOT = (os.path.join(BASE_DIR, 'static/'))
STATIC_URL = '/static/'
# STATICFILES_DIR = (os.path.join(BASE_DIR, 'static'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

AUTH_USER_MODEL = "hotelmanagement.CustomUser"
AUTHENTICATION_BACKENDS = ['hotelmanagement.EmailBackEnd.EmailBackEnd']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# """
# Django settings for AkachaRestaurant project.

# Generated by 'django-admin startproject' using Django 4.2.4.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.2/ref/settings/
# """

# from pathlib import Path
# import os

# import dj_database_url
# import environ

# env = environ.Env()

# environ.Env.read_env()

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env("SECRET_KEY")

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# ALLOWED_HOSTS = ['*']

# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     # 'elasticemailbackend',
#     # 'djrill',
#     # 'sms',

#     'hotelmanagement',
#     'StockManagerApp',
#     'EmailApp',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'AkachaRestaurant.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             os.path.normpath(os.path.join(BASE_DIR, 'templates')),
#         ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'hotelmanagement.processor.user_type_list',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'AkachaRestaurant.wsgi.application'

# # Database
# # https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# # DATABASES = {
# #     "default": dj_database_url.parse(env("DATABASE_URL"))
# # }

# # Password validation
# # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # Internationalization
# # https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.2/howto/static-files/

# # if 'DJANGO_SETTINGS_MODULE' in os.environ:
# #     # Production settings
# #     STATIC_ROOT = (os.path.join(BASE_DIR, 'static/'))
# # else:
# #     # Development settings
# STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static'),
#     ]
    

# STATIC_ROOT = (os.path.join(BASE_DIR, 'static/'))
# STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# AUTH_USER_MODEL = "hotelmanagement.CustomUser"
# # AUTHENTICATION_BACKENDS = (
# #     'hotelmanagement.EmailBackEnd.EmailBackEnd',
# # )

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Email Settings
# # DEFAULT_FROM_EMAIL = "manyerere201@gmail.com"
# # EMAIL_BACKEND = 'elasticemailbackend.backend.ElasticEmailBackend'
# # ELASTICEMAIL_API_KEY = '6CE59081AF3E89613C696A6738677D09333854132FB9857B476584BAEDF9A15EA8BC96F1442300C783FED0EB598927BB'

# # EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
# # MANDRILL_API_KEY = '27954D4610C8FDA10DD9DA75D8645089103516CA7F974BAF4A79915F6DA29D55D1AC270BBB416358CC9223CF7767F0DF'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# # EMAIL_HOST = 'smtp.elasticemail.com'
# # EMAIL_PORT = 2525
# # EMAIL_USE_TLS = True
# # EMAIL_USE_SSL = False
# # EMAIL_HOST_USER = 'manyerere201@gmail.com'
# # EMAIL_HOST_PASSWORD = '60062d40a3413812664f252d62b08d59'

# # EMAIL_HOST = 'smtp.sendgrid.net'
# # EMAIL_PORT = 25
# # EMAIL_USE_TLS = True
# # EMAIL_HOST_USER = 'apikey'
# # EMAIL_HOST_PASSWORD = '7ejCV29NqXPs61mAQlMXUUAOtSMquEuU'

# # MAILCHIMP_API_KEY = 'ed94a621a05d489d278a2e0c9952d92e-us21'
# # MAILCHIMP_LIST_ID = '7136a05b56'

# TWILLIO_ACCOUNT_SID = 'SKa383992c58ca633572af69c62afd8473'
# TWILLIO_AUTH_TOKEN = '57ccbaaaa717ae61fb949da7b808078e'

# # import mailtrap as mt
# #
# # mail = mt.Mail(
# #     sender=mt.Address(email="mailtrap@example.com", name="MailTrap Test"),
# #     to=[mt.Address(email="manyerere201@gmail.com")],
# #     subject="You are awesome",
# #     text="COngrats for sending your first email",
# # )
# #
# # client = mt.MailtrapClient(token="60062d40a3413812664f252d62b08d59")
# # # client = mt.MailtrapClient(token="1696308438")
# # client.send(mail)

# # from twilio.rest import Client
# #
# # account_sid = "SKa383992c58ca633572af69c62afd8473"
# # auth_token = "57ccbaaaa717ae61fb949da7b808078e"
# # client = Client(account_sid, auth_token)
# # message = client.messages.create(
# #     body="Hi there from Django",
# #     from_= "+17272337364",
# #     to="+255742106833"
# # )
# # print(message.sid)
