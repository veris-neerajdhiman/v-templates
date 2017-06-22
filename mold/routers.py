#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.routers
~~~~~~~~~~~~~~

- This file contains mold router
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.conf.urls import url

# local

# own app

from mold import views

UUID_REGEX = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

template_list = views.TemplateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

template_detail = views.TemplateViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update'
})

urlpatterns = [
    url(r'^templates/$',
        template_list,
        name='templates-list'),
    url(r'^templates/(?P<uuid>{uuid})/$'.format(uuid=UUID_REGEX),
        template_detail,
        name='templates-detail'),
]
