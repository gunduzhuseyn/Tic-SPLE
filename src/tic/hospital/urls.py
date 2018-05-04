from django.urls import path, include, re_path

from .views import (CreateHospitalEventView, ListHospitalEventView, HospitalEventView, HospitalEventReserveView,
                    ListHospitalTicketView, HospitalTicketView, HospitalTicketPurchaseView
					)

urlpatterns = [
    path('', include('core.urls')),
    path('event/new/', CreateHospitalEventView.as_view(), name='create_hospital_event'),
    path('event/all/', ListHospitalEventView.as_view(), name='list_hospital_event'),
    path('ticket/all/', ListHospitalTicketView.as_view(), name='list_plane_ticket'),
    re_path('event/(?P<pk>\d+)/$', HospitalEventView.as_view(), name='hospital_event_detail'),
    re_path('event/(?P<pk>\d+)/reserve/$', HospitalEventReserveView.as_view(), name='plane_event_reserve'),
    re_path('ticket/(?P<pk>\d+)/$', HospitalTicketView.as_view(), name='hospital_ticket_detail'),
    re_path('ticket/(?P<pk>\d+)/purchase/$', HospitalTicketPurchaseView.as_view(), name='hospital_ticket_purchase'),
]
