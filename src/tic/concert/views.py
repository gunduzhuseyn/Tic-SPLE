from datetime import datetime, timedelta

from django.contrib.auth.models import Group, User

from django.urls import reverse_lazy

from django.shortcuts import redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import ConcertEvent
# from .models import Event
from .forms import ConcertEventForm, SeatingPlanCreateForm

def is_user_cc(user):
	return user.groups.filter(name='content_creator').exists()

@method_decorator(user_passes_test(is_user_cc, login_url=reverse_lazy("error_403")), name='dispatch')
class CreatePlaneEventView(FormView):
	template_name = "concert/create_concert_event.html"
	form_class = ConcertEventForm
	success_url = reverse_lazy("create_concert_seating_plan")

	def form_valid(self, form):
		event = ConcertEvent.objects.create()
		event.name = form.cleaned_data.get('name')
		event.description = form.cleaned_data.get('description')
		event.location = form.cleaned_data.get('location')
		event.start_time = form.cleaned_data.get('start_time')
		event.end_time = form.cleaned_data.get('end_time')
		event.save()
		self.request.session['event_id'] = event.id
		return super().form_valid(form)

@method_decorator(user_passes_test(is_user_cc, login_url=reverse_lazy("error_403")), name='dispatch')
class CreateSeatingPlanView(FormView):
	template_name = "plane/create_seating_plan.html"
	form_class = SeatingPlanCreateForm
	success_url = '/concert/home/'		#reverse_lazy("list_plane_event")

	def get(self, request):
		if request.session.get('event_id'):
			return super().get(request)
		else:
			return redirect(reverse_lazy("error_404"))

	def form_valid(self, form):
		row_no = form.cleaned_data.get('row_no')
		col_no = form.cleaned_data.get('col_no')
		price = form.cleaned_data.get('price')
		event = ConcertEvent.objects.get(id=self.request.session.get('event_id'))
		seating_plan = event.seatingplan_set.create()
		seating_plan.row_no = row_no
		seating_plan.col_no = col_no
		seating_plan.save()
		num_of_seats = row_no * col_no
		for i in range(1, num_of_seats+1):
			seat = seating_plan.seat_set.create(seat_no=i)
			event.concertticket_set.create(price=price, seat=seat)
		
		event.save()
		del self.request.session['event_id']
		return super().form_valid(form)

# @method_decorator(login_required, name='dispatch')
# class PlaneEventReserveView(DetailView, FormView):
# 	model = PlaneEvent
# 	template_name = "plane/plane_event_reserve.html"
# 	context_object_name = 'event'
# 	form_class = ChooseSeatForm
# 	success_url = "/plane/ticket/all"

# 	def form_valid(self, form):
# 		event = self.get_object()
# 		seating_plan = event.seatingplan_set.all()[0]
# 		seat_no = int(form.cleaned_data.get('seat_no'))
# 		if seat_no < 1 or seat_no > (seating_plan.row_no * seating_plan.col_no):
# 			return redirect(reverse_lazy("error_404"))

# 		seat = seating_plan.seat_set.get(seat_no=seat_no)

# 		if not seat.is_empty:
# 			return redirect(reverse_lazy("error_404"))

# 		ticket = event.planeticket_set.get(seat=seat)
# 		seat.is_empty = False
# 		seat.save()
# 		ticket.is_reserved = True
# 		ticket.reserve_deadline = event.start_time - timedelta(days=1)
# 		ticket.owner = self.request.user
# 		ticket.save()

# 		return super().form_valid(form)

class ConcertEventView(DetailView):
	model = ConcertEvent
	template_name = "plane/plane_event_view.html"
	context_object_name = 'event'

# @method_decorator(login_required, name='dispatch')
# class PlaneTicketView(DetailView):
# 	model = PlaneTicket
# 	template_name = "plane/plane_ticket_view.html"
# 	context_object_name = 'ticket'

# @method_decorator(login_required, name='dispatch')
# class PlaneTicketPurchaseView(PlaneTicketView, FormView):
# 	template_name = "plane/plane_ticket_purchase.html"
# 	form_class = ButtonForm
# 	success_url = reverse_lazy("plane_ticket_detail")

# 	def form_valid(self, form):
# 		ticket = self.get_object()
# 		balance = self.request.user.useraccount.balance
# 		if balance < ticket.price:
# 			return redirect(reverse_lazy("error_410"))

# 		self.request.user.useraccount.balance = balance - ticket.price
# 		self.request.user.useraccount.save()
# 		ticket.is_purchased = True
# 		ticket.save()
# 		return redirect(reverse_lazy("plane_ticket_detail", kwargs={'pk':ticket.id}))

class ListConcertEventView(ListView):
	model = ConcertEvent
	paginate_by = 25
	template_name = "plane/plane_event_list.html"
	context_object_name = 'plane_event_list'
	ordering = ['name']

# @method_decorator(login_required, name='dispatch')
# class ListPlaneTicketView(ListView):
# 	model = PlaneTicket
# 	paginate_by = 25
# 	template_name = "plane/plane_ticket_list.html"
# 	context_object_name = 'plane_ticket_list'

# 	def get_queryset(self):
# 		return PlaneTicket.objects.filter(owner=self.request.user)