#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#       - Main settings file of CompuSoft.          #
#                                                   #
#####################################################

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!%^a8a3lf*rpjw!5wd8ni=6k5ubh2$+yv632%%=q_&+_k1uk$q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.0.102']

CUR_DOMAIN = os.environ.get('CUR_DOMAIN', 'localhost')

# Application definition
INSTALLED_APPS = [
    'voting.apps.VotingConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'compusoft.urls'

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

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

WSGI_APPLICATION = 'compusoft.wsgi.application'

# DATABASES
DATABASES_LIST = {
    'produccion': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dap5u3ni1bfndq',
        'USER': 'egltmpehffvmtt',
        'PASSWORD': '7000b7b0f3abb309ab8e7d63d069f5d9058f03aa0aacb0b342200c858d8c4eff',
        'HOST': 'ec2-204-236-239-225.compute-1.amazonaws.com',
        'PORT': '5432',
    },
    'localhost': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'compusoft',
        'USER': 'compusoft',
        'PASSWORD': 'compusoft',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

DATABASES = {
    'default': DATABASES_LIST[CUR_DOMAIN]
}

####################################################

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

# Login redirection
LOGIN_URL = '/login/'

# Accont activation email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'compushowusb@gmail.com'
EMAIL_HOST_PASSWORD = 'pizzabrownie11'
EMAIL_PORT = 587