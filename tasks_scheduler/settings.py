"""
Django settings for tasks_scheduler project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's@@i0y8ax9wl%)($5(1n*(wg^_8g97st65e_5*1m_$oxo+0zzv'

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
    'rest_framework',
    # 'guardian',
    'rest_auth',
    'rest_framework_swagger',
    'django_celery_beat',
    #
    'user_management'

]

# celery 配置
CELERY_BROKER_URL = 'amqp://admin:admin@localhost:5672/celery'
CELERY_RESULT_BACKEND = 'amqp://admin:admin@localhost:5672/celery'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_MAX_TASKS_PER_CHILD = 100  # 每个worker最多执行N个任务就会被销毁，可防止内存泄露
CELERY_BROKER_HEARTBEAT = None  # 如果不设置None, 会每隔一段时间连接中断一次
CELERY_CONCURRENCY = 20  # 并发worker数
# CELERY_TASK_TIME_LIMIT = 60    # 单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死
CELERY_FORCE_EXECV = True  # 非常重要,有些情况下可以防止死锁

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.normalize_response.NormalizeResponseMiddleware',

]

# rest_framework 配置
REST_FRAMEWORK = {

    # 身份认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 用于Swagger
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    # 禁用api接口页面
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),

    # 分页
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
}

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'guardian.backends.ObjectPermissionBackend',
# )

ROOT_URLCONF = 'tasks_scheduler.urls'

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

WSGI_APPLICATION = 'tasks_scheduler.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# swagger 配置项
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
}

# rest_auth
REST_USE_JWT = True

# JWT 配置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}
