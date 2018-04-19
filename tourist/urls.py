from django.conf.urls import url
from tourist.views import *

urlpatterns = [
    url(r'^$', TouristListView.as_view(), name='tourist_list'),
    url(r'^(?P<pk>\d+)/$', TouristDetailView.as_view(), name='tourist_detail'),
]