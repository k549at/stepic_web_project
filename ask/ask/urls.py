from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^ask/', include('ask.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','qa.views.index'),
    url(r'^login/','qa.views.test'),
    url(r'^signup/.*$','qa.views.test'),
    url(r'^question/<[0-9]*>','qa.views.test'),
    url(r'^ask/.*$','qa.views.test'),
    url(r'^popular/','qa.views.test'),
    url(r'^new/','qa.views.test'),
)
