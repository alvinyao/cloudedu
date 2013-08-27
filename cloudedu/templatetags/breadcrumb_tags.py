#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-24 02:24:26
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

import re
import copy
import pprint

from django import template
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

from django.template import Node, NodeList, Variable, Library
from django.template import TemplateSyntaxError, VariableDoesNotExist


def parse_args_kwargs(parser, token):
	contents = token.split_contents()
	tag_name = contents[0]
	args_list = contents[1:]
	args = []
	kwargs = {}
	
	for value in args_list:
		if '=' in value:
			k, v = value.split('=', 1)
			kwargs[str(k)] = v
		else:
			args.append(value)
	
	return tag_name, args, kwargs


class CaktNode(Node):
	def __init__(self, *args, **kwargs):
		self.args = [Variable(arg) for arg in args]
		self.kwargs = dict([(k, Variable(arg)) for k, arg in kwargs.items()])
		
	def render_with_args(self, context, *args, **kwargs):
		raise Exception('render_with_args must be implemented the class that inherits CaktNode')
	
	def render(self, context):
		args = []
		for arg in self.args:
			try:
				args.append(arg.resolve(context)) 
			except VariableDoesNotExist:
				args.append(None)
		
		kwargs = {}
		for k, arg in self.kwargs.items():
			try:
				kwargs[k] = arg.resolve(context)
			except VariableDoesNotExist:
				kwargs[k] = None
		
		return self.render_with_args(context, *args, **kwargs)

register = template.Library()

class AddCrumbNode(CaktNode):
	def render_with_args(self, context, crumb, url=None, *args):
		href = None
		if url:
			if '/' in url:
				href = url
			else:
				href = reverse(url, args=args)
		if 'request' in context:
			if not hasattr(context['request'], 'breadcrumbs'):
				context['request'].breadcrumbs = []
			context['request'].breadcrumbs.append((crumb, href))
		return ''


@register.tag
def add_crumb(parser, token):
	tag_name, args, kwargs = parse_args_kwargs(parser, token)
	return AddCrumbNode(*args, **kwargs)


@register.inclusion_tag('crumbs.html', takes_context=True)
def render_breadcrumbs(context):
	if 'request' in context and hasattr(context['request'], 'breadcrumbs'):
		crumbs = context['request'].breadcrumbs
	else:
		crumbs = None
	if crumbs and len(crumbs) == 1:
		crumbs = None
	return {
		'crumbs': crumbs,
	}
