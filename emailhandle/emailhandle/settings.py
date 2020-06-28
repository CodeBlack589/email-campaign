"""
Django settings for emailhandle project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gz6x(%9g)*s-xn+9lhf6)3nf(hzd33orkppb0c#h$a_@x3r6yi'

# SECURITY WARNING: don't run with debug turned on in production!
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
    'accounting',
     'allauth',   # <--
    'allauth.account',   # <--
    'allauth.socialaccount',   # <--
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'django_mongoengine',
    'django_mongoengine.mongo_auth',
    'django_mongoengine.mongo_admin',
    'emailaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emailhandle.urls'

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

WSGI_APPLICATION = 'emailhandle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

MONGODB_DATABASES={

}
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
         'CLIENT': {
            'host': "mongodb+srv://865tinkcomm243:91ty75we2mj@cluster0-er1jf.mongodb.net/email?retryWrites=true&w=majority"
        },
            'NAME': 'email',
    }
}
ENCRYPT_KEY=b'5MEX8QxOWv1IVrjdbKurwoWAofgqc_McDfWssAayzew='
ENCRYPT_KEY2=b'FXjnFBbIFsY8LoVDZ7CxcqiqjdjqP4AVWYEfy7XX2zY='
ENCRYPT_KEY3=b'608_X9rk9uos43XzXGkA8ya-FNMs-cIx-THsW_Nx35E='
ENCRYPT_KEY4=b'GaJ6sut-sRyFA1nwzQ5FkzC5q9fQSkkDXp03Z7ohzy0='

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
SITE_ID=1

#AUTH_USER_MODEL = 'mongo_auth.MongoUser'
#MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'
MEDIA_ROOT=os.path.join(BASE_DIR,'TinkComm')
MEDIA_URL='/TinkComm/'