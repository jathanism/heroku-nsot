# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
from nsot.conf.settings import *
import os

import dj_database_url


DATABASES = {
    'default': dj_database_url.config()
}


SECRET_KEY = u'fMK68NKgazLCjjTXjDtthhoRUS8IV4lwD-9G7iVd2Xs='

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

# USER_AUTH_HEADER = 'X-Pp-User'

STATIC_ROOT = 'static_root'

DEBUG = True
