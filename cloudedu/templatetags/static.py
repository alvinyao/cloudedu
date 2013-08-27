#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-20 22:01:37
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

from django.conf import settings                                                   
from django.template import Library                                                
                                                                                   
register = Library()                                                               
                                                                                   
if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:                        
    from django.contrib.staticfiles.templatetags.staticfiles import static         
else:                                                                              
    from django.templatetags.static import static                                  
                                                                                   
static = register.simple_tag(static)                                                                                                                 

