from django.contrib.auth.models import Group, User

from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from .models import PlaneEvent, SeatingPlan, Seat
from .forms import PlaneEventForm, SeatingPlanForm

class CreatePlaneEventView(FormView):
	template_name = "plane/create_plane_event.html"
	form_class = PlaneEventForm
	success_url = reverse_lazy("create_seating_plan")

	def form_valid(self, form):
		event = PlaneEvent.objects.create()
		event.name = form.cleaned_data.get('name')
		event.description = form.cleaned_data.get('description')
		event.location = form.cleaned_data.get('location')
		event.location_to = form.cleaned_data.get('location_to')
		event.save()
		self.request.session['event_id'] = event.id
		return super().form_valid(form)

class CreateSeatingPlanView(FormView):
	template_name = "plane/create_seating_plan.html"
	form_class = SeatingPlanForm
	success_url = "/home/"

	def form_valid(self, form):
		row_no = form.cleaned_data.get('row_no')
		col_no = form.cleaned_data.get('col_no')
		seating_plan = SeatingPlan.objects.create()
		seating_plan.row_no = row_no
		seating_plan.col_no = col_no
		seating_plan.save()
		num_of_seats = row_no * col_no
		for i in range(1, num_of_seats+1):
			seat = seating_plan.seat_set.create(seat_no=i)
		return super().form_valid(form)