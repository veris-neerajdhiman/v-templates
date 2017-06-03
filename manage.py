#!/usr/bin/env python
import os, sys, re

from django.core.exceptions import ImproperlyConfigured
from config.load_env_variables import read_env

if __name__ == '__main__':
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    try:
        # read Environment file
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config/local/env_file')
        read_env(env_file)
        # read_env()
        execute_from_command_line(sys.argv)
    except ImproperlyConfigured:
        raise ImproperlyConfigured(
            '-------WARNING--------- \n'
            'Settings are not configured correctly\n'
        )

