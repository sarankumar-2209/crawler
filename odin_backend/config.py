# config.py
import os
from pathlib import Path
import logging

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-t!6w-5co7rxl(!3w7t#di2=d1+lbk1p=#=9x_-7ynanip5cj*-'
DEBUG = True
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "crawler",
    'corsheaders',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend", "dist")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Razorpay Configuration
RAZORPAY_CONFIG = {
    'KEY_ID': "rzp_live_JCExPjTteNgBfp",
    'KEY_SECRET': "FIzzzQeXFAJRACGj4TRjojYd",
    'WEBHOOK_SECRET': "Winner@2003",
    'PLAN_ID': "plan_QDLsfNsqsxULWn",
    'SUBSCRIPTION_ID': "sub_QDRfqjnj567L55",
    'SUBSCRIPTION_LINK': "https://rzp.io/rzp/NOdF9p5b",
    'WEBHOOK_URL': "https://astraeusnextgen.com/verification"
}

# Scraper Configuration
SCRAPER_CONFIG = {
    'USER_AGENTS': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    ],
    'TIMEOUT': 30,
    'MAX_RETRIES': 3
}

# Security Scanner Configuration
SECURITY_SCANNER_CONFIG = {
    'COMMON_PORTS': [80, 443, 8080, 22, 21, 3389, 3306, 5432, 27017],
    'TIMEOUT': 5,
    'THREADS': 50
}

# Dark Web Scanner Configuration
DARKWEB_CONFIG = {
    'TOR_PORTS': [(9150, "Tor Browser"), (9050, "Tor Service"), (9151, "Tor Browser (alternative)")],
    'RESOURCES': [
        ("http://darkfailllnkf4vf.onion", "DarkFail", "search", "Search Engine"),
        ("http://grams7enufi7jmdl.onion", "Grams", "search", "Search Engine"),
        ("https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion", "DuckDuckGo", "search", "Search Engine"),
        ("http://torrezmarket.onion", "Torrez Market", "market", "Marketplace"),
        ("http://monopolyymv3mioq.onion", "Monopoly Market", "market", "Marketplace"),
        ("http://dreadditevelidot.onion", "Dread Forum", "forum", "Forum")
    ],
    'TIMEOUT': 45
}

# File Analysis Configuration
FILE_ANALYSIS_CONFIG = {
    'TEXT_FILE_EXTENSIONS': ['.txt', '.log', '.csv', '.json', '.py', '.js', '.html', '.css'],
    'IMAGE_EXTENSIONS': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'VIDEO_EXTENSIONS': ['.mp4', '.mov', '.avi', '.mkv']
}