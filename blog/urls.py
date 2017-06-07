from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^post/$', views.home, name='home'),
    url(r'^post/(?P<id>[0-9]+)/$', views.view_post, name='post'),
    url(r'^add/$', views.add_post, name='add_post'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit_post, name='edit_post'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.del_post, name='del_post'),



]
