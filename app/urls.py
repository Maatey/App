from django.conf.urls import url

from app.views import (main_view,
                       ProjectView,
                       get_project,
                       get_project_detail,
                       post_project,
                       get_question,
                       get_answer, post_answer)

urlpatterns = [
    url('main', main_view, name='main'),
    url(r'get_project', get_project, name='get_project'),
    url(r'^(?P<pk>\d+)/$', get_project_detail, name='project_detail'),
    url('post_project/', post_project, name='post_project'),
    url('get_question/', get_question, name='get_question'),
    url('get_answer/', get_answer, name='get_answer'),
    url('post_answer/', post_answer, name='post_answer'),
    url('pro/', ProjectView.as_view()),
    ]