#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-23 19:14:07
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:
'''
from django.conf.urls import patterns, include, url
from views import DataDictList, DataDictCreate, DataDictDelete, DataDictUpdate

urlpatterns = patterns('essential.views',
    url(r'^$', DataDictList.as_view(), name='essential-index'),
    url(r'^add/$', DataDictCreate.as_view(), name='datadict-add'),
    url(r'^(?P<pk>\d+)/$', DataDictUpdate.as_view(), name='datadict-update'),
    url(r'^(?P<pk>\d+)/delete/$', DataDictDelete.as_view(), name='datadict-delete'),
)
'''

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.simple import direct_to_template

from crud import views as crud_views
import views, models

urlpatterns = patterns('',

	url(r'^datadict/$', views.ListView.as_view(), name='datadict-list'),

    url(r'^datadict/add/$', views.CreateView.as_view(), 
		name='datadict-add'),

    url(r'^datadict/(?P<pk>\d+)$', views.DetailView.as_view(), 
		name = 'datadict-detail'),

    url(r'^datadict/update/(?P<pk>\d+)$', crud_views.UpdateView.as_view(
			model=models.DataDict), 
		name = 'datadict-update'),

    url(r'^datadict/delete/(?P<pk>\d+)$', views.DeleteView.as_view(
			model=models.DataDict,
			success_url = reverse_lazy('datadict-list')),
        name = 'datadict-delete'),

)
