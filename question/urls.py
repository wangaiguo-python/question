from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_category, name='category'),
    url(r'^question/(?P<id>\d+)/$',views.show_question, name='question'),
    url(r'^answer/(?P<id>\d+)/$', views.show_answer, name='answer'),
]