from django.db import models

from core.models import Event, Ticket, CoreSeatingPlan, CoreSeat

class PlaneEvent(Event):
	location_to = models.CharField(max_length=500, default='')
	flight_number = models.CharField(max_length=50, default='')

class SeatingPlan(CoreSeatingPlan):
	event = models.ForeignKey(PlaneEvent, on_delete=models.CASCADE, default=None)

class Seat(CoreSeat):
	seating_plan = models.ForeignKey(SeatingPlan, on_delete=models.CASCADE)

class PlaneTicket(Ticket):
	event = models.ForeignKey(PlaneEvent, on_delete=models.CASCADE)
	seat = models.OneToOneField(Seat, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.event.name)