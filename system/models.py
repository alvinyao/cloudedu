#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-26 21:52:27
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

from django.db import models
from django.contrib.contenttypes.models import ContentType
from auth.models import User, AuthModel, Group
from system.util import quote
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe

ADDITION = 1
CHANGE = 2
DELETION = 3

class LogEntryManager(models.Manager):
    def log_action(self, user_id, content_type_id, object_id, object_repr, action_flag, change_message=''):
        e = self.model(None, None, user_id, content_type_id, smart_unicode(object_id), object_repr[:200], action_flag, change_message)
        e.save()

class LogEntry(models.Model):
    action_time = models.DateTimeField(_('action time'), auto_now=True)
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.TextField(_('object id'), blank=True, null=True)
    object_repr = models.CharField(_('object repr'), max_length=200)
    action_flag = models.PositiveSmallIntegerField(_('action flag'))
    change_message = models.TextField(_('change message'), blank=True)

    objects = LogEntryManager()

    class Meta:
        verbose_name = _('log entry')
        verbose_name_plural = _('log entries')
        db_table = 'django_admin_log'
        ordering = ('-action_time',)

    def __repr__(self):
        return smart_unicode(self.action_time)

    def __unicode__(self):
        if self.action_flag == ADDITION:
            return _('Added "%(object)s".') % {'object': self.object_repr}
        elif self.action_flag == CHANGE:
            return _('Changed "%(object)s" - %(changes)s') % {'object': self.object_repr, 'changes': self.change_message}
        elif self.action_flag == DELETION:
            return _('Deleted "%(object)s."') % {'object': self.object_repr}

        return _('LogEntry Object')

    def is_addition(self):
        return self.action_flag == ADDITION

    def is_change(self):
        return self.action_flag == CHANGE

    def is_deletion(self):
        return self.action_flag == DELETION

    def get_edited_object(self):
        "Returns the edited object represented by this log entry"
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def get_admin_url(self):
        """
        Returns the admin URL to edit the object represented by this log entry.
        This is relative to the Django admin index page.
        """
        if self.content_type and self.object_id:
            return mark_safe(u"%s/%s/%s/" % (self.content_type.app_label, self.content_type.model, quote(self.object_id)))
        return None
    
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    sort_code = models.CharField(verbose_name = u'排序编号', max_length=255)
    realname = models.CharField(verbose_name = u'真实姓名', max_length=255)
    #staff = models.CharField(verbose_name = u'关联职工', max_length=255)
    
    
class GroupProfile(models.Model):
    auth_model = models.ForeignKey(AuthModel)
    group = models.ForeignKey(Group)
    is_active = models.BooleanField(verbose_name = u'是否激活', default=True)
    desc = models.CharField(verbose_name = u'描述', max_length=511)
    

