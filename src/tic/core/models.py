from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=100, default='')
	profile_image = models.ImageField(upload_to='images', blank=True)

	def __str__(self):
		return self.user.username

class UserAccount(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

class Event(models.Model):
	name = models.CharField(max_length = 250)
	description = models.TextField()
	location = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Ticket(models.Model):
	price = models.IntegerField(default=0)
	is_reserved = models.BooleanField(default=False)
	is_purchased = models.BooleanField(default=False)
	reserve_deadline = models.DateTimeField()
	owner = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

	def __str__(self):
		return self.event.name

class Schedule(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()

	def __str__(self):
		return "schedule"

