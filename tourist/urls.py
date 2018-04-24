from django.conf.urls import url
from tourist.views import *

urlpatterns = [
    url(r'^$', TouristListView.as_view(), name='tourist_list'),
    url(r'^(?P<pk>\d+)/$', TouristDetailView.as_view(), name='tourist_detail'),
    url(r'^new/$', tourist_create, name='tourist_create'),
    url(r'^(?P<pk>\d+)/update/$', tourist_edit, name='tourist_edit'),
    url(r'^(?P<pk>\d+)/delete/$', TouristDeleteView.as_view(), name='tourist_delete'),
]