from django.conf.urls import patterns, url
from qa import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)
