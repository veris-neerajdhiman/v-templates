#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.views
~~~~~~~~~~~~

- This file contains Template micro-service views, every HTTP request/router points to this file.
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework
from rest_framework import viewsets, permissions

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
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'uuid'

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,  # request object is passed here
        }

    def get_queryset(self):
        """

        :return: Template queryset
        """
        qs = super(TemplateViewSet, self).get_queryset()

        return qs.filter(user=self.request.user)
