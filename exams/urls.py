from django.conf.urls import url
from . import api
from django.views.generic.base import TemplateView

urlpatterns = [
    # questions api urls
    url(r'^questions/$', api.QuestionListView.as_view(), name='ques-list'),
    url(r'^questions/create/$', api.QuestionView.as_view(), name='ques-create'),
    url(r'^questions/detail/(?P<pk>[0-9]+)/$', api.QuestionDetailView.as_view(), name='ques-detail'),
    url(r'^questions/edit/(?P<pk>[0-9]+)/$', api.QuestionView.as_view(), name='ques-edit'),
    url(r'^questions/delete/(?P<pk>[0-9]+)/$', api.QuestionView.as_view(), name='ques-delete'),
    # exam api urls
    url(r'^exams/$', api.ExamListView.as_view(), name='exam-list'),
    url(r'^exams/create/$', api.ExamView.as_view(), name='exam-create'),
    url(r'^exams/detail/(?P<pk>[0-9]+)/$', api.ExamView.as_view(), name='exam-detail'),
    url(r'^exams/edit/(?P<pk>[0-9]+)/$', api.ExamView.as_view(), name='exam-edit'),
    url(r'^exams/delete/(?P<pk>[0-9]+)/$', api.ExamView.as_view(), name='exam-delete'),
    # response api urls
    url(r'^responses/$', api.ResponseListView.as_view(), name='response-list'),
    url(r'^responses/create/$', api.ResponseView.as_view(), name='response-create'),
    url(r'^responses/detail/(?P<pk>[0-9]+)/$', api.ResponseDetailView.as_view(), name='response-detail'),
    url(r'^responses/edit/(?P<pk>[0-9]+)/$', api.ResponseView.as_view(), name='response-edit'),
    url(r'^responses/delete/(?P<pk>[0-9]+)/$', api.ResponseView.as_view(), name='response-delete'),
    # template urls
    url(r'^exam-portal/signup/$', TemplateView.as_view(template_name="login_signup.html"), name='processtemp-view'),
    url(r'^exam-portal/exams/$', TemplateView.as_view(template_name="examanee.html"), name='processtemp-view'),
    url(r'^exam-portal/home/$', TemplateView.as_view(template_name="home.html"), name='processtemp-view'),
    url(r'^exam-portal/admin/$', TemplateView.as_view(template_name="admin.html"), name='processtemp-view'),
    url(r'^exam-portal/examanees/$', TemplateView.as_view(template_name="examanees.html"), name='processtemp-view'),
]
