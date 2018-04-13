from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^board/(?P<pk>\d+)/$', views.board_detail, name='board_detail'),
    url(r'^board/new/$', views.board_new, name='board_new'),
    url(r'^board/(?P<pk>\d+)/comment/$',views.add_comment_to_post, name='add_comment_to_post'),
]
