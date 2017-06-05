from django.conf.urls import url
from polls import views
from polls.views import QuestionDetailView


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', QuestionDetailView.as_view(), name='question_detail'),
    url(r'^(?P<id>[0-9]+)/result/$', views.question_result, name='view_result'),
    url(r'^(?P<id>[0-9]+)/vote/$', views.question_vote, name='vote'),

]
