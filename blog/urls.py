from django.conf.urls import url

from blog import views
from blog.views import home

urlpatterns = [
    url(r'^post/$', home, name='home'),
    url(r'^post/(?P<id>[0-9]+)/$', views.view_post, name='view_post')

]
