from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^$', views.homepage, name='homepage'),
    
    # /andy
    url(r'^username=(?P<username>[a-z]+)/$', views.userpage, name='userpage'),

    # /andy/1
    url(r'^username=(?P<username>[a-z]+)/(?P<playlist>[0-9]+)/$', views.playlist, name='playlist'),
]