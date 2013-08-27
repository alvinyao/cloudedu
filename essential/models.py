#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-24 01:29:39
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

import datetime
from django.core.urlresolvers import reverse
from django.db import models
from crud.models import CRUDModelMixin

# Create your models here.

class DataDict(CRUDModelMixin, models.Model):
	code = models.CharField(max_length=255, verbose_name = u'代码')
	name = models.CharField(max_length=255, verbose_name = u'代码名称')
	status = models.BooleanField(verbose_name = u'状态')
	order = models.IntegerField(verbose_name = u'排序编号')
	created = models.DateTimeField(null=True, default=datetime.datetime.now(), verbose_name = u'创建时间')
	modified = models.DateTimeField(null=True, default=datetime.datetime.now(), verbose_name = u'更新时间')

	def __unicode__(self):
		return u'%s' % self.name

	class Meta:                                                                
		verbose_name = u'数据字典'                                               
		verbose_name_plural = u'数据字典'                                        

