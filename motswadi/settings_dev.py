from motswadi.settings import *

DEBUG = True
CREATE_DEFAULT_SUPERUSER = True

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'motswadi.sqlite'

INSTALLED_APPS = INSTALLED_APPS + (
    'snippetscream',
)
