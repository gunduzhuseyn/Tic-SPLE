from django.contrib import admin

from .models import HospitalEvent, HospitalTicket

admin.site.register(HospitalEvent)
admin.site.register(HospitalTicket)
