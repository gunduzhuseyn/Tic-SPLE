from django.contrib import admin

from .models import ConcertEvent, SeatingPlan, Seat, ConcertTicket

admin.site.register(ConcertEvent)
admin.site.register(SeatingPlan)
admin.site.register(Seat)
admin.site.register(ConcertTicket)