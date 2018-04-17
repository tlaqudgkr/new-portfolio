from django.conf.urls import url
from hotel.views import *

urlpatterns = [
    url(r'^$', HotelListView.as_view(), name='hotel_list'),
    url(r'^(?P<pk>\d+)/$', HotelDetailView.as_view(), name='hotel_detail'),
    url(r'^new/$', hotel_create, name='hotel_create'),
    url(r'^$', RoomListView.as_view(), name='room_list'),
    url(r'^$', FacilityListView.as_view(), name='facility_list'),
]