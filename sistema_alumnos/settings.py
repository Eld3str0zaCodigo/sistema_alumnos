import os
from pathlib import Path
import dj_database_url
import pymysql

# 1. ESTO DEBE IR ARRIBA DE TODO PARA ENGAÑAR A DJANGO
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

# ... (resto de tu configuración de SECRET_KEY, DEBUG, APPS, etc.) ...

# 2. CONFIGURACIÓN DE BASE DE DATOS (REEMPLAZA TU BLOQUE DATABASES)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        # IMPORTANTE: Forzamos el backend de MySQL aquí
        engine='django.db.backends.mysql',
        conn_max_age=600,
    )
}

# ... (resto de tu archivo) ...


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de WhiteNoise para comprimir archivos y caché
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'