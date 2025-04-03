import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'odin_backend.settings')  # Change 'odin_backend' to your actual project name

application = get_wsgi_application()
