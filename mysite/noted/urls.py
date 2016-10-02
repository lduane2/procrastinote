from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'noted'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^(?P<upload_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^upload/$', views.upload_file, name='upload'),
    #url(r'^uploaded/(?P<file_id>[0-9]+)/$', views.uploaded, name='upload_file'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
