from django.conf.urls import url
from . import views

app_name = 'noted'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<file_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^upload/$', views.upload_file, name='upload'),
    #url(r'^uploaded/(?P<file_id>[0-9]+)/$', views.uploaded, name='upload_file'),
]
