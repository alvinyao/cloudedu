#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-26 22:46:55
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

import django_tables2 as tables

class Table(tables.Table):
	class Meta:
		attrs = {
				'class': 'table table-striped table-bordered table-hover'
			}
