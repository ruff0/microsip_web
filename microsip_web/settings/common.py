# Django settings for libreria project.
#encoding:utf-8

# Identificando la ruta del proyecto
import os
import fdb
RUTA_PROYECTO =os.path.dirname(os.path.realpath(__file__)).strip('settings')
DIR = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASE_ROUTERS = ['microsip_web.libs.custom_db.databases_routers.MainRouter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.firebird', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'C:\Microsip datos\DJANGO.FDB',
        'USER': 'SYSDBA',                      # Not used with sqlite3.
        'PASSWORD': 'masterkey',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3050',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS' : {'charset':'ISO8859_1'},
    },
    'config': {
       'ENGINE': 'django.db.backends.firebird', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'C:\Microsip datos\System\CONFIG.FDB',
        'USER': 'SYSDBA',                      # Not used with sqlite3.
        'PASSWORD': 'masterkey',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3050',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS' : {'charset':'ISO8859_1'},
    },
}

MICROSIP_DATABASES = {}

db= fdb.connect(host="localhost",user="SYSDBA",password="masterkey",database="C:\Microsip datos\System\CONFIG.FDB")
cur = db.cursor()
cur.execute("SELECT NOMBRE_CORTO FROM EMPRESAS")
empresas_rows = cur.fetchall()



for empresa in empresas_rows:
    MICROSIP_DATABASES[empresa[0].replace(' ','_')] = {
        'ENGINE': 'django.db.backends.firebird', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': u'C:\Microsip datos\%s.FDB'% empresa[0],
        'USER': 'SYSDBA',                      # Not used with sqlite3.
        'PASSWORD': 'masterkey',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3050',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS' : {'charset':'ISO8859_1'},
    }

    DATABASES[empresa[0].replace(' ','_')] = {
        'ENGINE': 'django.db.backends.firebird', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': u'C:\Microsip datos\%s.FDB'% empresa[0],
        'USER': 'SYSDBA',                      # Not used with sqlite3.
        'PASSWORD': 'masterkey',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3050',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS' : {'charset':'ISO8859_1'},
    }



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Mazatlan'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-mx'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
MEDIA_URL = os.path.join(RUTA_PROYECTO,'media/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',

)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3pq$&amp;*)sd$k_olmn@lup_5)-)d=qk-&amp;)18!+5bw7+$z++n2jm@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'microsip_web.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    (RUTA_PROYECTO + '/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#Configuraciones para enviar mensajes usando gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'remitente@gmail.com'
EMAIL_HOST_PASSWORD = 'clavedelcorreo'
EMAIL_PORT = 587
