from django.db import models

from core.models import Event, Ticket

class PlaneEvent(Event):
	# seating_plan = models.OneToOneField(SeatingPlan, on_delete=models.CASCADE, default=None, null=True)
	location_to = models.CharField(max_length=500, default='')
	flight_number = models.CharField(max_length=50, default='')

class SeatingPlan(models.Model):
	row_no = models.IntegerField(default=0)
	col_no = models.IntegerField(default=0)
	plane_event = models.ForeignKey(PlaneEvent, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return "row: " + str(self.row_no) + "\tcol: " + str(self.col_no)

class PlaneTicket(Ticket):
	plane_event = models.ForeignKey(PlaneEvent, on_delete=models.CASCADE)

	def __str__(self):
		return self.plane_event.name

class Seat(models.Model):
	seat_no = models.IntegerField(default=0)
	is_empty = models.BooleanField(default=True)
	seating_plan = models.ForeignKey(SeatingPlan, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.seat_no)