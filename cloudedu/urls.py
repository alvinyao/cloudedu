from django.conf.urls import patterns, include, url
from system import site
import system
system.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cloudedu.views.index', name='index'),
    url(r'^essential/', include('essential.urls')),
    url(r'^system/', include(site.urls)),
)

