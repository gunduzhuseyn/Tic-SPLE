from django.db import models

from core.models import Event, CoreSeatingPlan, CoreSeat, Ticket

class ConcertEvent(Event):
	pass

class SeatingPlan(CoreSeatingPlan):
	event = models.ForeignKey(ConcertEvent, on_delete=models.CASCADE, default=None)

class Seat(CoreSeat):
	seating_plan = models.ForeignKey(SeatingPlan, on_delete=models.CASCADE)

class ConcertTicket(Ticket):
	event = models.ForeignKey(ConcertEvent, on_delete=models.CASCADE)
	seat = models.OneToOneField(Seat, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.event.name)