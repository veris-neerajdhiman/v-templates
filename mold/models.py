#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- mold.models
~~~~~~~~~~~~~~

- This file holds the necessary models for Templates micro-service
"""

# future
from __future__ import unicode_literals

# 3rd party
import uuid

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

# local


# own app


class Templates(models.Model):
    """Templates model

    """

    # Attributes
    uuid = models.UUIDField(
            _('Template uuid'),
            unique=True,
            default=uuid.uuid4,
            editable=False,
            help_text=_('Non-editable, to be generated by system itself.'),
    )
    name = models.CharField(
            _('Template Name'),
            max_length=255,
            null=False,
            blank=False,
            help_text=_('Template Name.'),
    )
    description = models.TextField(
            _('Template Description'),
            help_text=_('Template Description.'),
    )
    schema = JSONField(
        _('Template schema.'),
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
                 _('created at'),
                 auto_now_add=True,
                 db_index=True,
    )
    modified_at = models.DateTimeField(
                 _('modified at'),
                 auto_now=True,
                 db_index=True,
    )

    # Meta
    class Meta:
        verbose_name = _("Template")
        verbose_name_plural = _("Templates")

    # Functions
    def __str__(self):
        return '{name} : {uuid}'.format(
            name=self.name,
            uuid=self.uuid
        )
