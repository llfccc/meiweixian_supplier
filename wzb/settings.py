# coding=utf-8
"""
Django settings for wzb project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import os.path

PythonLocal=os.environ.get( "PythonLocal" )


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 've#a40)!-a8&obbaj(e^@k0uu%yp(hzpq&s+wm!3fjm_o3+nvw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["182.61.46.28",'127.0.0.1', 'localhost','192.168.8.179','chubang.duapp.com']


# Application definition

INSTALLED_APPS = [
    'wzb',
    'order',
    'bootstrap3',
    # 'supplierList',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    # 'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'stockCode',
    'el_pagination',
    # 'notifications',
    # 'keyEvent',
    #'debug_toolbar',


]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'wzb.urls'



STATIC_ROOT = '/data/meiwei/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join('static'), )

#扩展user字段
# AUTH_USER_MODEL = "wzb.NewUser"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/'],
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

WSGI_APPLICATION = 'wzb.wsgi.application'


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'EJBBUUwqChHOLVCZcLLR',  # 你的数据库名称
            'USER': 'root',  # 你的数据库用户名
            'PASSWORD': 'root',  # 你的数据库密码
            'HOST': '127.0.0.1',  # 你的数据库主机，留空默认为localhost
            'PORT': '3306',  # 你的数据库端口
        }
    }



#if PythonLocal:
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.mysql',
#            'NAME': 'GoGTrxkomIYhBYaRgrZG',  # 你的数据库名称
#            'USER': 'root',  # 你的数据库用户名
#            'PASSWORD': 'root',  # 你的数据库密码
#            'HOST': '127.0.0.1',  # 你的数据库主机，留空默认为localhost
#            'PORT': '3306',  # 你的数据库端口
#        }
#    }
#else:
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.mysql',
#            'NAME': 'EJBBUUwqChHOLVCZcLLR',  # 你的数据库名称
#            'USER': 'e9907f8bffa44bda802a0ef2bb6899c2',  # 你的数据库用户名
#            'PASSWORD': 'b06b2908f86d4c4ebdba351b335f0a37',  # 你的数据库密码
#            'HOST': 'sqld.duapp.com',  # 你的数据库主机，留空默认为localhost
#            'PORT': '4050',  # 你的数据库端口
#        }
#    }
#

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

#日志设置
# if PythonLocal:
#     LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }, # 针对 DEBUG = True 的情况
#     },
#     'formatters': {
#         'standard': {
#             'format': '%(levelname)s %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d: %(message)s'
#         }, # 对日志信息进行格式化，每个字段对应了日志格式中的一个字段，更多字段参考官网文档，我认为这些字段比较合适，输出类似于下面的内容
#         # INFO 2016-09-03 16:25:20,067 /home/ubuntu/mysite/views.py views.py views get 29: some info...
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter':'standard'
#         },
#         'file_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'logging/byod.admin.log',
#             'formatter':'standard'
#         }, # 用于文件输出
#         'console':{
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers' :['file_handler', 'console'],
#             'level':'DEBUG',
#             'propagate': True # 是否继承父类的log信息
#         }, # handlers 来自于上面的 handlers 定义的内容
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         }
#     }

# LOGGING = {
#     'version': 1, # 标示配置模板版本，int 类型，目前只接收 `1`这个值。
#     'disable_existing_loggers': False, # 这个没太看明白什么意思，了解的朋友麻烦说明下
#     'formatters': {
#         'standard': {
#              'format': '%(levelname)s %(asctime)s %(message)s',
#         },
#     },
#     'filters': {
#         # 这里是定义过滤器，需要注意的是，由于 'filters' 是 logging.config.dictConfig 方法要求在配置字典中必须给订的 key ,所以即使不使用过滤器也需要明确给出一个空的结构。
#     },
#     'handlers': {
#          'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter':'standard',
#         },
#         'tofile': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'formatter':'standard',
#             'filename': 'logging/view.log',
#         },
#     },
#     'loggers': {
#         'project.app': {
#             'handlers': ['tofile'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     }
# }

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Shanghai'
#TIME_ZONE = 'UTC'
USE_TZ = False
USE_I18N = True

USE_L10N = True

EL_PAGINATION_PER_PAGE=20


BASE_DIR = (os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# INTERNAL_IPS = ('192.168.8.179',)
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda request: not request.is_ajax() and request.META.get('REMOTE_ADDR', None) in INTERNAL_IPS
# }