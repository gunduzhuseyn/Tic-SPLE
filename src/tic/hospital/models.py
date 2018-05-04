from django.db import models

from core.models import Event, Ticket

class HospitalEvent(Event):
	duration = models.CharField(max_length=50, default='')
	pass

class HospitalTicket(Ticket):
	start_time = models.DateTimeField(null=True)
	end_time = models.DateTimeField(null=True)
	event = models.ForeignKey(HospitalEvent, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.event.name)

