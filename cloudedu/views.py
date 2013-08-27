#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-21 11:25:46
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

from django.template.response import TemplateResponse

def index(request, template='index.html'):
	return TemplateResponse(request, template, {})

