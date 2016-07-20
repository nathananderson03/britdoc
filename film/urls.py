# film urls
from django.conf.urls import patterns, url
from film import views

urlpatterns = patterns('',
    url(r'index/$', views.index, name='index'),
    url(r'^display/([a-zA-Z0-9-]+)/$', views.display, name='display'),
    url(r'^fund/([a-zA-Z0-9-]+)/$', views.fund, name='fund'),
    url(r'^subject/([a-zA-Z0-9-]+)/$', views.subject, name='subject'),
    url(r'^year/([0-9-]+)/$', views.year, name='year'),
    url(r'^alpha/([A-Z])/$', views.alpha, name='alpha'),
)
