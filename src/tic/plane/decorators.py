def create_seating_plan(function):
	def wrap(request, *args, **kwargs):
		if request.session.get('event_id'):
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/home/')