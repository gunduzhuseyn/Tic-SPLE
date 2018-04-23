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

class Schedule(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()

	def __str__(self):
		return "schedule"

class Event(models.Model):
	name = models.CharField(max_length = 250, default='')
	description = models.TextField(default='')
	location = models.CharField(max_length=500, default='')
	schedule = models.OneToOneField(Schedule, default=None, on_delete=models.SET_DEFAULT)

	def __str__(self):
		return self.name

	class Meta:
		abstract = True

class Ticket(models.Model):
	price = models.IntegerField(default=0)
	is_reserved = models.BooleanField(default=False)
	is_purchased = models.BooleanField(default=False)
	reserve_deadline = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, null=True)
	schedule = models.OneToOneField(Schedule, default=None, on_delete=models.SET_DEFAULT)

	class Meta:
		abstract = True



