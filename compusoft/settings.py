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

ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.0.102', 'compushow2018.herokuapp.com']

CUR_DOMAIN = os.environ.get('CUR_DOMAIN', 'localhost')

DEBUG = CUR_DOMAIN == 'localhost'

# Application definition
INSTALLED_APPS = [
    'voting.apps.VotingConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages'
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

WSGI_APPLICATION = 'compusoft.wsgi.application'

# DATABASES

DB_PASS = os.environ.get('DB_PASS', '')

DATABASES_LIST = {
    'produccion': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dap5u3ni1bfndq',
        'USER': 'egltmpehffvmtt',
        'PASSWORD': DB_PASS,
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
    },
    'testing': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'debq3251djvgu9',
        'USER': 'yrndhlrvagjtqd',
        'PORT': '5432',
        'PASSWORD': '895a8c8ab829258ae88220196262a225e4f729eabb33999935266f95cda1c9b8',
        'HOST': 'ec2-54-204-18-53.compute-1.amazonaws.com',
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

if CUR_DOMAIN != 'localhost':
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_LOCATION = 'static'

    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Login redirection
LOGIN_URL = '/login/'

# Accont activation email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'compushowusb@gmail.com'
EMAIL_HOST_PASSWORD = 'pizzabrownie11'
EMAIL_PORT = 587