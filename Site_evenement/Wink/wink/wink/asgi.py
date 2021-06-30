"""
WSGI config for wink project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import django
from channels.routing import get_default_application
from django.core.wsgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wink.settings')
django.setup()
application = get_default_application()
