from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from datetime import date

from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=52)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)

class ContentCreatorRegistrationForm(forms.Form):
	username = forms.CharField(label="Username", max_length=50)
	email = forms.EmailField(label="Email", max_length=52)


class LoginForm(forms.Form):
	username = forms.CharField(label="Username", max_length=50)
	password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

class UserProfileEditForm(forms.Form):
	email = forms.EmailField(label="Email", max_length=52, required=False)
	first_name = forms.CharField(label="First Name", max_length=50, required=False)
	last_name = forms.CharField(label="Last Name", max_length=50, required=False)
	bio = forms.CharField(label="Bio", max_length=50, required=False)
	profile_image = forms.ImageField(label="Profile Image", required=False)

class PaymentForm(forms.Form):
	number = forms.CharField(min_length=16, max_length=16, label="Card Number")
	name = forms.CharField(label="Card Holder Name", max_length=30)
	expire_month = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)])
	expire_year = forms.ChoiceField(choices=[(x, x) for x in range(date.today().year, date.today().year + 15)])
	cvv_number = forms.IntegerField(label="CVV Number", max_value=9999, widget=forms.TextInput(attrs={'size':'4'}))
	amount = forms.IntegerField(label="Amount")
