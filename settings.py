# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

from django.utils.crypto import get_random_string
import dj_database_url
from nsot.conf.settings import *
import os


# Use Heroku's $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config()
}

# This is so that we can use Heroku's SSL properly
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# To generate a secret_key in your Heroku config, run this:
# $ heroku config:set SECRET_KEY=`openssl rand -base64 32`
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
)

AUTH_TOKEN_EXPIRY = 600 * 3  # 30 minutes

###############
# Application #
###############

# The address on which the application will listen.
# Default: localhost
NSOT_HOST = '0.0.0.0'

# The port on which the application will be accessed.
# Default: 8990
NSOT_PORT = os.getenv('PORT')

STATIC_ROOT = 'static_root'

DEBUG = True
