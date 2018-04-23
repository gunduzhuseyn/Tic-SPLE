from django.contrib import admin

from .models import PlaneEvent, SeatingPlan, Seat, PlaneTicket

admin.site.register(PlaneEvent)
admin.site.register(SeatingPlan)
admin.site.register(Seat)
admin.site.register(PlaneTicket)
