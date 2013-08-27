#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-26 21:52:27
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

import django_tables2 as tables
from crud.columns import CheckBoxColumn

from models import *

class UserProfileTable(tables.Table):
	id = CheckBoxColumn(attrs = {'th': {'class':'center', 'style':'width:30px'}, 'td': {'class':'center'}, 'input':{'class': 'ace'}})

	class Meta:
		model = UserProfile
		fields = ('id','sort_code','user.username', 'realname', 'user.is_active','user.date_joined' )
		attrs = {
			'id': 'user-table',
			'class': 'table table-striped table-bordered table-hover dataTable'
		}
		
class GroupProfileTable(tables.Table):
	id = CheckBoxColumn(attrs = {'th': {'class':'center', 'style':'width:30px'}, 'td': {'class':'center'}, 'input':{'class': 'ace'}})

	class Meta:
		model = GroupProfile
		fields = ('id','group.name','auth_model.name', 'is_active', 'desc')
		attrs = {
			'id': 'user-table',
			'class': 'table table-striped table-bordered table-hover dataTable'
		}
		
		



