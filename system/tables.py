#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-26 21:52:27
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

from crud import views as crud_views
from auth import User

class ListView(crud_views.ListView):
	model = User
	queryset = DataDict.objects.all()
	table_class = UserTable
	table_pagination = {'per_page': 10}


