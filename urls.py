from django.conf.urls import patterns, include, url
from gtdserver.api import *
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
v1 = Api(api_name='v1')
v1.register(GtdResource())
v1.register(RegionResource())
v1.register(CountryResource())
v1.register(AlternativeResource())
v1.register(AttackTypeResource())
v1.register(TargetTypeResource())
v1.register(ClaimModeResource())
v1.register(WeaponTypeResource())
v1.register(WeaponSubtypeResource())
v1.register(PropExtentResource())
v1.register(HostageOutcomeResource())
v1.register(DbsourceResource())

urlpatterns = patterns('',
                       (r'^api/', include(v1.urls)),
    # Examples:
    # url(r'^$', 'gtdserver.views.home', name='home'),
    # url(r'^gtdserver/', include('gtdserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
