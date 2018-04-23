from django.contrib.auth.models import Group, User

from django.urls import reverse_lazy

from django.shortcuts import redirect

from django.utils.decorators import method_decorator

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .decorators import create_seating_plan

from .models import PlaneEvent, SeatingPlan, Seat
from .forms import PlaneEventForm, SeatingPlanForm
from core.forms import ScheduleForm

class CreatePlaneEventView(FormView):
	template_name = "plane/create_plane_event.html"
	form_class = PlaneEventForm
	form_class_2 = ScheduleForm
	success_url = reverse_lazy("create_seating_plan")

	def get_context_data(self, **kwargs):
		context = super(CreatePlaneEventView, self).get_context_data(**kwargs)
		context['form2'] = self.form_class_2()
		return context


	def form_valid(self, form):
		event = PlaneEvent.objects.create()
		event.name = form.cleaned_data.get('name')
		event.description = form.cleaned_data.get('description')
		event.location = form.cleaned_data.get('location')
		event.location_to = form.cleaned_data.get('location_to')
		event.flight_number = form.cleaned_data.get('flight_number')
		event.save()
		self.request.session['event_id'] = event.id
		return super().form_valid(form)

class CreateSeatingPlanView(FormView):
	template_name = "plane/create_seating_plan.html"
	form_class = SeatingPlanForm
	success_url = "/home/"

	def get(self, request):
		if request.session.get('event_id'):
			return super().get(request)
		else:
			return redirect(reverse_lazy("error_404"))

	def form_valid(self, form):
		row_no = form.cleaned_data.get('row_no')
		col_no = form.cleaned_data.get('col_no')
		price = form.cleaned_data.get('price')
		event = PlaneEvent.objects.get(id=self.request.session.get('event_id'))
		seating_plan = event.seatingplan_set.create()
		seating_plan.row_no = row_no
		seating_plan.col_no = col_no
		seating_plan.save()
		num_of_seats = row_no * col_no
		for i in range(1, num_of_seats+1):
			seating_plan.seat_set.create(seat_no=i)
			event.planeticket_set.create(price=price)
		
		event.seating_plan = seating_plan
		
		event.save()
		del self.request.session['event_id']
		return super().form_valid(form)

class PlaneEventView(DetailView):
	model = PlaneEvent
	template_name = "plane/plane_event_view.html"
	context_object_name = 'event'

class ListPlaneEventView(ListView):
	model = PlaneEvent
	paginate_by = 25
	template_name = "plane/plane_event_list.html"
	context_object_name = 'plane_event_list'