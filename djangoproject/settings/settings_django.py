SITE_ID = 1

# Make this unique, and don't share it with anybody. Set to none so django
# will complain

SECRET_KEY = None

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'stracksapp.middleware.StracksMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'stracksapp.middleware.TimezoneMiddleware'
)

ROOT_URLCONF = 'stracksite.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'stracksapp',
    'stracksapi',
    'stracks_api', ## mostly for testing purposes, has no role in stracksapp/site
    'two.ol',
    'two.bootstrap',
    'two.userauth',
    'twotest',
)

