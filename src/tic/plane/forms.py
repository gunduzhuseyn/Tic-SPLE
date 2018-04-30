from django import forms

from .models import PlaneEvent
from core.forms import CoreSeatingPlanForm, CoreSeatingPlanCreateForm, CoreChooseSeatForm, CoreButtonForm

class PlaneEventForm(forms.ModelForm):
	class Meta:
		model = PlaneEvent
		exclude = ['schedule']
		labels = {'location': 'Departure', 'location_to':'Destination'}

class SeatingPlanForm(CoreSeatingPlanForm):
	pass

class SeatingPlanCreateForm(CoreSeatingPlanCreateForm):
	pass

class ChooseSeatForm(CoreChooseSeatForm):
	pass

class ButtonForm(CoreButtonForm):
	pass

class SeatPriceForm(forms.Form):
	default = forms.CharField(max_length=30, label="Default price for all seats")

	def __init__(self, *args, **kwargs):
		seat_count = kwargs.pop('seat_count')
		super(SeatPriceForm, self).__init__(*args, **kwargs)

		for i in range(seat_count):
			self.fields['seat_%s' %i] = forms.CharField(max_length=30, label="Price for Seat %s" %i)