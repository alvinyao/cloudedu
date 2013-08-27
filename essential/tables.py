#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-26 21:52:27
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

import django_tables2 as tables
from crud.columns import CheckBoxColumn

from models import DataDict

class DataDictTable(tables.Table):
	id = CheckBoxColumn(attrs = {'th': {'class':'center', 'style':'width:30px'}, 'td': {'class':'center'}, 'input':{'class': 'ace'}})
	code = tables.Column()
	name = tables.Column()

	class Meta:
		model = DataDict
		fields = ('id', 'code', 'name', 'status')
		attrs = {
			'id': 'datadict-table',
			'class': 'table table-striped table-bordered table-hover dataTable'
		}

