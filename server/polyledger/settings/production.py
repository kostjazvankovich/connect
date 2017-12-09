from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = '/var/www/app.polyledger.com/staticfiles'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "/var/www/app.polyledger.com/staticfiles"),
]

POSTGRESQL_NAME = os.environ.get('POSTGRESQL_NAME')
POSTGRESQL_USER = os.environ.get('POSTGRESQL_USER')
POSTGRESQL_PASSWORD = os.environ.get('POSTGRESQL_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSTGRESQL_NAME,
        'USER': POSTGRESQL_USER,
        'PASSWORD': POSTGRESQL_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
CSRF_TRUSTED_ORIGINS = ['app.polyledger.com']
