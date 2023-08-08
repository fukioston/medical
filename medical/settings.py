"""
Django settings for medical project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i2&z&$*j8tbgp$q06!w3+6=--+5^4q090w!15eh-nabk#24rs!'

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

    # django APP
    'user.apps.UserConfig',
    'graph.apps.GraphConfig',
    'robot.apps.RobotConfig',
    'calculate.apps.CalculateConfig',
    'column.apps.ColumnConfig',
    'map.apps.MapConfig',
    'statistic.apps.StatisticConfig',
'manager.apps.ManagerConfig',
    # 富文本编辑器
    'ckeditor',
    'ckeditor_uploader'
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

ROOT_URLCONF = 'medical.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': []
        ,
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

WSGI_APPLICATION = 'medical.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

disease_path = os.path.join(BASE_DIR, 'utils\\robot\data\disease.txt')
deny_path = os.path.join(BASE_DIR, 'utils\\robot\data\deny.txt')
drug_path = os.path.join(BASE_DIR, 'utils\\robot\data\drug.txt')
food_path = os.path.join(BASE_DIR, 'utils\\robot\data\\food.txt')
symptom_path = os.path.join(BASE_DIR, 'utils\\robot\data\symptom.txt')
department_path = os.path.join(BASE_DIR, 'utils\\robot\data\department.txt')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = 'static/images/column/articles'
CKEDITOR_JQUERY_URL = 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_RESTRICT_BY_DATE = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (['Source', '-', 'Preview', '-', ],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', ],
                    ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat', '-',
                     "CodeSnippet", 'Subscript', 'Superscript'],
                    ['NumberedList', 'BulletedList', '-', 'Blockquote'],
                    ['Link', 'Unlink', ],
                    ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', ],
                    ['Format', 'Font', 'FontSize', 'TextColor', 'BGColor', ],
                    ['Bold', 'Italic', 'Underline', 'Strike', ],
                    ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ),
        'extraPlugins': 'codesnippet',
        'height': '500px',
        'width': 'auto',
    }
}

try:
    from .local_settings import *
except ImportError:
    pass
