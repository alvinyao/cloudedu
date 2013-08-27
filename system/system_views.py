#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-26 21:52:27
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

from crud import views as crud_views
from models import UserProfile, GroupProfile
from tables import *

class UserView(crud_views.ListView):
	model = UserProfile
	queryset = UserProfile.objects.all()
	table_class = UserProfileTable
	table_pagination = {'per_page': 10}
	
class GroupView(crud_views.ListView):
	model = GroupProfile
	queryset = GroupProfile.objects.all()
	table_class = GroupProfileTable
	table_pagination = {'per_page': 10}
    
