import os
from decouple import config
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"core.settings.{config('AMBIENT')}")

application = get_wsgi_application()
