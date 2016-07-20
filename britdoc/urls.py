from django.conf.urls import include, url
from django.contrib import admin

# next 2 for dev server only
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # static pages for main content
    url(r'^funds/$', 'core.views.funds', name='funds'),
    url(r'^bertha-connect/$', 'core.views.berthaconnect', name='bertha-connect'),
    url(r'^bertha-journalism/$', 'core.views.berthajournalism', name='bertha-journalism'),
    url(r'^britdoc-circle/$', 'core.views.britdoccircle', name='britdoc-circle'),
    url(r'^resources/$', 'core.views.resources', name='resources'),

    url(r'^projects/$', 'core.views.projects', name='projects'),

    url(r'^films/', include('film.urls', namespace='film', app_name='film')),

    url(r'^contact/$', 'core.views.contact', name='contact'),
    url(r'^mailout_signup/$', 'core.views.mailout_signup', name='mailout_signup'),
    url(r'^mailout_preview/$', 'core.views.mailout_preview', name='mailout_preview'),


    url(r'^admin/', include(admin.site.urls)),

    url(r'^redactor/', include('redactor.urls')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
