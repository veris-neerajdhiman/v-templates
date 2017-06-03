"""
WSGI config for veris project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from config.load_env_variables import read_env

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.local.settings")

# read Environment file
env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'env_file')
read_env(env_file)

application = get_wsgi_application()
