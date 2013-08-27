from django.conf.urls import patterns, include, url
from system import system_views

urlpatterns = patterns('',
    url(r'^$', system_views.UserView.as_view(), name='user-list'),
    url(r'^group$', system_views.GroupView.as_view(), name='group-list'),
)

