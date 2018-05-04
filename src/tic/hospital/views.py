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

from .models import HospitalEvent, HospitalTicket
from .forms import HospitalEventForm, ChooseTicketForm, ButtonForm

def is_user_cc(user):
	return user.groups.filter(name='content_creator').exists()

@method_decorator(user_passes_test(is_user_cc, login_url=reverse_lazy("error_403")), name='dispatch')
class CreateHospitalEventView(FormView):
	template_name = "hospital/create_hospital_event.html"
	form_class = HospitalEventForm
	success_url = '/hospital/event/all/'

	def form_valid(self, form):
		event = HospitalEvent.objects.create()
		event.name = form.cleaned_data.get('name')
		event.description = form.cleaned_data.get('description')
		event.location = form.cleaned_data.get('location')
		event.start_time = form.cleaned_data.get('start_time')
		event.end_time = form.cleaned_data.get('end_time')
		event.duration = form.cleaned_data.get('duration')
		price = form.cleaned_data.get('price')

		#generate tickets
		
		interval = timedelta(minutes=int(event.duration))
		begin = event.start_time + interval
		end = event.end_time
		while begin < end:
			event.hospitalticket_set.create(price=price, start_time=begin - interval, end_time=begin)
			begin = begin + interval

		event.save()
		return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class HospitalEventReserveView(DetailView, FormView):
	model = HospitalEvent
	template_name = "hospital/hospital_event_reserve.html"
	context_object_name = 'event'
	form_class = ChooseTicketForm
	success_url = "/hospital/ticket/all"

	def form_valid(self, form):
		event = self.get_object()

		start = form.cleaned_data.get('start')
		end = form.cleaned_data.get('end')

		ticket_set = event.hospitalticket_set.filter(start_time=start, end_time=end)

		if ticket_set:
			ticket = ticket_set[0]
			if ticket.is_reserved or ticket.is_purchased:
				return redirect(reverse_lazy("error_404"))

			ticket.is_reserved = True
			ticket.reserve_deadline = ticket.end_time - timedelta(hours=6)
			ticket.owner = self.request.user
			ticket.save()

			return super().form_valid(form)
		else:
			return redirect(reverse_lazy("error_404"))

class HospitalEventView(DetailView):
	model = HospitalEvent
	template_name = "hospital/hospital_event_view.html"
	context_object_name = 'event'

@method_decorator(login_required, name='dispatch')
class HospitalTicketView(DetailView):
	model = HospitalTicket
	template_name = "hospital/hospital_ticket_view.html"
	context_object_name = 'ticket'

@method_decorator(login_required, name='dispatch')
class HospitalTicketPurchaseView(HospitalTicketView, FormView):
	template_name = "hospital/hospital_ticket_purchase.html"
	form_class = ButtonForm
	success_url = reverse_lazy("hospital_ticket_detail")

	def form_valid(self, form):
		ticket = self.get_object()
		balance = self.request.user.useraccount.balance
		if balance < ticket.price:
			return redirect(reverse_lazy("error_410"))

		self.request.user.useraccount.balance = balance - ticket.price
		self.request.user.useraccount.save()
		ticket.is_purchased = True
		ticket.save()
		return redirect(reverse_lazy("hospital_ticket_detail", kwargs={'pk':ticket.id}))

class ListHospitalEventView(ListView):
	model = HospitalEvent
	paginate_by = 25
	template_name = "hospital/hospital_event_list.html"
	context_object_name = 'event_list'
	ordering = ['name']

@method_decorator(login_required, name='dispatch')
class ListHospitalTicketView(ListView):
	model = HospitalTicket
	paginate_by = 25
	template_name = "hospital/hospital_ticket_list.html"
	context_object_name = 'ticket_list'

	def get_queryset(self):
		return HospitalTicket.objects.filter(owner=self.request.user)
