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
    url(r'^$','qa.views.main'),
    url(r'^login/','qa.views.test'),
    url(r'^signup/.*$','qa.views.test'),
#    url(r'^question/<[0-9]*>','qa.views.question',name='quest_det'),
    url (r'^question/(?P<pk>\d+)/$','qa.views.question'),
    url (r'^question/(?P<pk>\d+)/answer','qa.views.answer'),
    url(r'^ask/.*$','qa.views.ask'),
    url(r'^popular/','qa.views.popular'),
    url(r'^new/','qa.views.answer'),
)
