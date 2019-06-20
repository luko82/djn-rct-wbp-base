"""
    Local settings
    ./manage.py shell --settings=backend.settings.dev
"""
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "%s/%s" % (BASE_DIR, 'db.sqlite3'),
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'STATS_FILE': "%s/%s" % (BASE_DIR.ancestor(1).child('frontend'), 'webpack-stats.json')
    }
}

