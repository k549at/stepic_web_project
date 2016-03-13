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
    #url(r'^$',''),
    #url(r'^login/',''),
    #url(r'^signup/.*$',''),
    url(r'^question/<[0-9]*>','qa.views.test'),
    #url(r'^ask/.*$',''),
    #url(r'^popular/',''),
    #url(r'^new/',''),
)
