from django.conf.urls.defaults import patterns, url
from .views import PackageTableView

urlpatterns = patterns('',
    url('^table/(?P<pk>\d+)/$', PackageTableView.as_view(), name="table"),
)
