#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.views
~~~~~~~~~~~~~~

- This file contains Template micro-service views, every HTTP request/router points to this file.
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status

# Django

# local

# own app
from mold import serializers, models


class TemplateViewSet(viewsets.ModelViewSet):
    """Template Viewset, every authorization http request handles by this class

    """
    model = models.Templates
    queryset = model.objects.all()
    serializer_class = serializers.TemplateSerializer
    # TODO : remove AllowAny permission with proper permission class
    permission_classes = (permissions.AllowAny, )
    lookup_field = 'uuid'

    def get_schema(self, request, uuid):
        """

        :param uuid: Template obj uuid
        :return: Template schema
        """
        response = serializers.TemplateSchemaSerializer(instance=self.get_object())

        return Response(response.data.get('schema'), status=status.HTTP_200_OK)
