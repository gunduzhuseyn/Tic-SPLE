from django import forms

from .models import (PlaneEvent, SeatingPlan)


class PlaneEventForm(forms.ModelForm):
	class Meta:
		model = PlaneEvent
		exclude = ['seating_plan']
		labels = {'location': 'Departure', 'location_to':'Destination'}

class SeatingPlanForm(forms.ModelForm):
	class Meta:
		model = SeatingPlan
		fields = '__all__'