from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^board/(?P<pk>\d+)/$', views.board_detail, name='board_detail'),
    url(r'^board/new/$', views.board_new, name='board_new'),
    url(r'^board/edit/(?P<pk>\d+)$', views.board_edit, name='board_edit'),
    url(r'^board/remove/(?P<pk>\d+)$', views.board_remove, name='board_remove'),

    url(r'^board/(?P<pk>\d+)/comment/$',views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
