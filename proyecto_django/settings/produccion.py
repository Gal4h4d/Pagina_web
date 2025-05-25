from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']  # Cambia por tu dominio real cuando tengas uno

# Configuración base de datos (SQLite, aunque en producción lo ideal es PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / get_secret('DB_NAME'),
    }
}

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # carpeta donde collectstatic guarda archivos

# Archivos de media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Middleware: añade WhiteNoise para servir estáticos sin necesidad de nginx
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Aquí debe ir WhiteNoise
    # el resto de tus middlewares del base.py ...
]

# Configura WhiteNoise para mejorar el rendimiento de archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
