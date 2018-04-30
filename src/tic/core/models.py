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
	name = models.CharField(max_length = 250, default='')
	description = models.TextField(default='')
	start_time = models.DateTimeField(null=True)
	end_time = models.DateTimeField(null=True)
	location = models.CharField(max_length=500, default='')

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

	class Meta:
		abstract = True

class CoreSeatingPlan(models.Model):
	row_no = models.IntegerField(default=0)
	col_no = models.IntegerField(default=0)

	def __str__(self):
		return "row: " + str(self.row_no) + "\tcol: " + str(self.col_no)

	class Meta:
		abstract = True

class CoreSeat(models.Model):
	seat_no = models.IntegerField(default=0)
	is_empty = models.BooleanField(default=True)

	def __str__(self):
		return str(self.seat_no)

	class Meta:
		abstract = True



