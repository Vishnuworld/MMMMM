"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.
sdsadadaaaaaaaaaaaaaa
ssssssssssssssssssss
sssssssssssssss
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
# oooooooooooooooooooooooooooooooooo
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_wsgi_application()
