from django import forms

from .models import HospitalEvent, HospitalTicket
from core.forms import CoreButtonForm

class HospitalEventForm(forms.ModelForm):
	duration = forms.CharField(label="Duration for each appointment", max_length=50)
	price = forms.CharField(label="Price for each appointment", max_length=50)

	class Meta:
		model = HospitalEvent
		exclude = ['schedule']
		labels = {'location': 'Location'}


class ChooseTicketForm(forms.Form):
	start = forms.DateTimeField(label='Start')
	end = forms.DateTimeField(label='End')

class ButtonForm(CoreButtonForm):
	pass
