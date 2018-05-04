from django.urls import path, include, re_path

from .views import (CreateConcertEventView, CreateSeatingPlanView, ConcertEventView, ListConcertEventView, ConcertEventReserveView,
                    ListConcertTicketView, ConcertTicketView, ConcertTicketPurchaseView
                    )


urlpatterns = [
    path('', include('core.urls')),
    path('event/new/', CreateConcertEventView.as_view(), name='create_concert_event'),
    path('event/new/seating_plan/', CreateSeatingPlanView.as_view(), name='create_concert_seating_plan'),
    path('event/all/', ListConcertEventView.as_view(), name='list_concert_event'),
    path('ticket/all/', ListConcertTicketView.as_view(), name='list_concert_ticket'),
    re_path('event/(?P<pk>\d+)/$', ConcertEventView.as_view(), name='concert_event_detail'),
    re_path('event/(?P<pk>\d+)/reserve/$', ConcertEventReserveView.as_view(), name='concert_event_reserve'),
    re_path('ticket/(?P<pk>\d+)/$', ConcertTicketView.as_view(), name='concert_ticket_detail'),
    re_path('ticket/(?P<pk>\d+)/purchase/$', ConcertTicketPurchaseView.as_view(), name='concert_ticket_purchase'),
] 


# url(r'^book/(?P<pk>\d+)/$', MyDetail.as_view(), name='book'),