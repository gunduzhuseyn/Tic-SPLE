from django.urls import path, include

from .views import (CreatePlaneEventView, CreateSeatingPlanView)
urlpatterns = [
    path('', include('core.urls')),
    path('event/new/', CreatePlaneEventView.as_view(), name='create_plane_event'),
    path('event/new/seating_plan/', CreateSeatingPlanView.as_view(), name='create_seating_plan')
] 
