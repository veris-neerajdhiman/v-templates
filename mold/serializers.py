# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.serializers
~~~~~~~~~~~~~~

- This file contains the Templates Serializers.
 """

# future
from __future__ import unicode_literals

# 3rd party

# DRF
from rest_framework import serializers

# Django
from django.conf import settings

# local

# own app
from mold import models


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    """

    """
    url = serializers.HyperlinkedIdentityField(
        view_name='{app_namespace}:templates-detail'.format(app_namespace=getattr(settings, 'APP_NAMESPACE')),
        lookup_field='uuid')

    class Meta:
        model = models.Templates
        fields = ('url', 'uuid', 'name', 'description', 'schema', )


class TemplateSchemaSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = models.Templates
        fields = ('schema', )
