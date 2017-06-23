#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.tests.test_settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file includes test-cases of settings which are required for Template micro-service

"""

# future
from __future__ import unicode_literals

# third party
import os

# Django
from django.conf import settings
from django.test import TestCase


class SettingsTestCase(TestCase):
    """Settings Test Case

    """

    pass


class EnvironmentVariableTestCase(TestCase):
    """Environment Variables Test case
    """
    def setUp(self):
        """
        """
        self.env_variables = (
            'DATABASE_NAME_TEMPLATE',
            'DATABASE_USER',
            'DATABASE_PASSWORD',
            'DATABASE_HOST',
            'DATABASE_PORT',
            'SECRET_KEY',
        )

    def test_env_variables(self):
        """Makes sure necessary env variables are declared.
        """
        for key in self.env_variables:
            try:
                return os.environ[key]
            except KeyError:
                self.assertFalse('{0} environment variable is not defined.'.format(key))