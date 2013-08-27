#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-24 01:29:39
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

from django.core import serializers
from django.template import Library

register = Library()

# Meta-data Extractors 
# -------------------------
@register.simple_tag()
def get_app_label( object ):
    """
    Returns the app label for an app.
    """
    return object._meta.app_label


@register.simple_tag()
def get_verbose_name( object ):
    """
    Returns the verbose name for a model.
    """
    return object._meta.verbose_name

@register.simple_tag()
def get_verbose_name_plural( object ):
    """
    Returns the verbose pluralized name for a model.
    """
    return object._meta.verbose_name_plural

# -------------------------
# Filters
# -------------------------

@register.filter
def model_to_dict( object ):
    """
    Converts a model into a dictionary of its fields and values.
    """
    return serializers.serialize( "python", [object] )[0]['fields']
