#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.tests.test_views
~~~~~~~~~~~~~~~~~~~~~~~

- This file includes Test cases for Views .

"""

# future
from __future__ import unicode_literals

# 3rd party
import json
from urllib.parse import urlencode

# Django
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

# local
from mold.models import Templates

TEMPLATE_SCHEMA = {
                "init": {
                    "sections": [{
                        "items": [{
                            "type": "vertical",
                            "components": [{
                                "name": "__caption__",
                                "type": "label",
                                "value": "Caption",
                                "style": {
                                    "fontSize": 14,
                                    "fontWeight": 700,
                                    "textTransform": "uppercase"
                                }
                            }, {
                                "name": "__heading__",
                                "type": "label",
                                "value": "Heading",
                                "style": {
                                    "fontSize": 36,
                                    "marginBottom": 8,
                                    "fontWeight": 700
                                }
                            }, {
                                "orientation": "horizontal",
                                "type": "divider"
                            }],
                            "style": {
                                "padding": 16,
                                "maxWidth": 512
                            }
                        }]
                    }]
                }
            }


class TemplatesTestCase(TestCase):
    """Handles Templates Views Test Cases

    """

    def setUp(self):
        """

        """
        self.template_josn = json.dumps(TEMPLATE_SCHEMA)

        self.template = Templates.objects.create(
            name='test-name',
            description='test-desc',
            schema=self.template_josn
        )

    def test_template_create(self):
        """Test Create Template Object

        """
        url = reverse('{0}:templates-list'.format(
            getattr(settings, 'APP_NAMESPACE')
        ))
        data = {
            'name': 'test-template',
            'description': 'template-desc',
            'schema': self.template_josn
        }
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 201)

    def test_template_list(self):
        """Test Template Object list

        """
        url = reverse('{0}:templates-list'.format(
            getattr(settings, 'APP_NAMESPACE')
        ))

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_template_detail(self):
        """Test Template Object details

        """
        url = reverse('{0}:templates-detail'.format(
            getattr(settings, 'APP_NAMESPACE')
        ), args=(self.template.uuid, ))

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_template_update(self):
        """Test Update Template Object

        """
        url = reverse('{0}:templates-detail'.format(
            getattr(settings, 'APP_NAMESPACE')
        ), args=(self.template.uuid, ))

        data = urlencode({
            'name': 'updated-test'
        })

        response = self.client.patch(url, content_type="application/x-www-form-urlencoded", data=data)

        self.assertEqual(response.status_code, 200)
