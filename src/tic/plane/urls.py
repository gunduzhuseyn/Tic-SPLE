from django.urls import path, include, re_path

from .views import (CreatePlaneEventView, CreateSeatingPlanView, PlaneEventView, ListPlaneEventView)
urlpatterns = [
    path('', include('core.urls')),
    path('event/new/', CreatePlaneEventView.as_view(), name='create_plane_event'),
    path('event/new/seating_plan/', CreateSeatingPlanView.as_view(), name='create_seating_plan'),
    path('event/all/', ListPlaneEventView.as_view(), name='list_plane_event'),
    re_path('event/(?P<pk>\d+)/$', PlaneEventView.as_view(), name='plane_event_detail'),
    # path('event/<slug:slug>/', PlaneEventView.as_view(), name='plane_event_detail'),
] 


# url(r'^book/(?P<pk>\d+)/$', MyDetail.as_view(), name='book'),