"""
    Production settings
    ./manage.py shell --settings=backend.settings.prod
"""
from .base import *

# Debug False implies that django won't serve statics
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "%s/%s" % (BASE_DIR, 'db.sqlite3'),
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': "%s/%s" % (BASE_DIR.ancestor(1).child('frontend'), 'webpack-stats.json')
    }
}
