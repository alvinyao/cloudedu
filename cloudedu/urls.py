from django.conf.urls import patterns, include, url
from system import site

urlpatterns = patterns('',
    url(r'^$', 'cloudedu.views.index', name='index'),
    url(r'^essential/', include('essential.urls')),
    url(r'^system/', include('system.urls')),
)


