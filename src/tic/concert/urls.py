from django.urls import path, include, re_path

from .views import CreatePlaneEventView, CreateSeatingPlanView, ConcertEventView


urlpatterns = [
    path('', include('core.urls')),
    path('event/new/', CreatePlaneEventView.as_view(), name='create_concert_event'),
    # path('event/all/', CreatePlaneEventView.as_view(), name='create_plane_event'),
    path('event/new/seating_plan/', CreateSeatingPlanView.as_view(), name='create_concert_seating_plan'),
    # path('event/all/', ListPlaneEventView.as_view(), name='list_plane_event'),
    # path('ticket/all/', ListPlaneTicketView.as_view(), name='list_plane_ticket'),
    re_path('event/(?P<pk>\d+)/$', ConcertEventView.as_view(), name='concert_event_detail'),
    # re_path('event/(?P<pk>\d+)/reserve/$', PlaneEventReserveView.as_view(), name='plane_event_reserve'),
    # re_path('ticket/(?P<pk>\d+)/$', PlaneTicketView.as_view(), name='plane_ticket_detail'),
    # re_path('ticket/(?P<pk>\d+)/purchase/$', PlaneTicketPurchaseView.as_view(), name='plane_ticket_purchase'),
    # path('event/<slug:slug>/', PlaneEventView.as_view(), name='plane_event_detail'),
] 


# url(r'^book/(?P<pk>\d+)/$', MyDetail.as_view(), name='book'),