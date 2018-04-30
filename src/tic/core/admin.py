from django.contrib import admin

from .models import UserProfile, UserAccount #, Schedule

admin.site.register(UserProfile)
admin.site.register(UserAccount)
# admin.site.register(Schedule)