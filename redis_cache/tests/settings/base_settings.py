DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
INSTALLED_APPS = [
    'redis_cache.tests.testapp',
]
ROOT_URLCONF = 'tests.urls'
SECRET_KEY = "shh...it's a seakret"
