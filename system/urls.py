from django.conf.urls import patterns, include, url
from system import site
import system
system.autodiscover()

urlpatterns = patterns('',
    url(r'^user/$', views.ListView.as_view(), name='user-list'),
)
