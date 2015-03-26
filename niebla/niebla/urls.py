from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    # url(r'^$', 'niebla.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^qa/', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
