import os
from decouple import config

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"core.settings.{config('AMBIENT')}")

application = get_asgi_application()
