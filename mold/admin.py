#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.admin
~~~~~~~~~~~~

- This file contains admin models of Template micro service
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.contrib import admin

# local

# own app
from mold import models


class TemplateAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'uuid', 'name', 'created_at', )
    list_display_links = ('id', 'name', )
    search_fields = ('id', 'uuid', 'name', )
    list_per_page = 20
    ordering = ('-id',)

admin.site.register(models.Templates, TemplateAdmin)


