from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, 
										PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, 
										PasswordChangeDoneView)

from django.contrib.admin.views.decorators import staff_member_required

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from .forms import (UserRegistrationForm, LoginForm, ContentCreatorRegistrationForm, UserProfileEditForm, PaymentForm)
from .models import (UserProfile, UserAccount)

#group_required decorator

def redi_url(path, url):
	if 'plane' in path:
		return '/plane/' + url + '/'
	elif 'concert' in path:
		return '/concert/' + url + '/'
	if 'hospital' in path:
		return '/hospital/' + url + '/'
	return '/' + url + '/'

def group_required(*group_names):
	def in_groups(u):
		if u.is_authenticated():
			if bool(u.is_superuser | u.groups.filter(name__in=group_names)):
				return True
			return False
		return user_passes_test(in_groups)

class HomeView(TemplateView):
	template_name = "core/home.html"

def create_accounts(user):
	profile = UserProfile.objects.create(user=user)
	profile.save()

	account = UserAccount.objects.create(user=user)
	account.save()

class CustomerRegistrationView(FormView):
	template_name = "core/registration/register.html"
	form_class = UserRegistrationForm
	success_url = 'home'

	def form_valid(self, form):
		self.success_url = redi_url(self.request.path, self.success_url)
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=raw_password)
		group = Group.objects.get(name='customer')
		group.user_set.add(user)
		login(self.request, user)

		create_accounts(self.request.user)

		return super().form_valid(form)

@method_decorator(staff_member_required(login_url='/403/'), name='dispatch')
class ContentCreatorRegistrationView(FormView):
	template_name = "core/registration/register.html"
	form_class = ContentCreatorRegistrationForm
	success_url = "home"

	def form_valid(self, form):
		self.success_url = redi_url(self.request.path, self.success_url)
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = User.objects.make_random_password()
		user = User.objects.create_user(username, email, password)
		
		email_subject = "Content Creator Credentials"
		email_body = "Below are your credentials to access Tic platform as a content creator. Please change your password as soon as you log in to Tic system!\nUsername: " + username + "\nPassword: " + password
		email_sender = "no_reply@tic.com"
		html_message = render_to_string("core/registration/ccregister_email.html", {'username': username, 'password':password})
		send_mail(email_subject, email_body, email_sender, [email,], html_message=html_message)
		user.save()
		group = Group.objects.get(name='content_creator')
		group.user_set.add(user)

		create_accounts(user)

		return super().form_valid(form)

class UserLoginView(LoginView):
	template_name = "core/registration/login.html"

	def get_redirect_url(self):
		if 'concert' in self.request.path:
			return '/concert/home/'
		elif 'plane' in self.request.path:
			return '/plane/home/'
		elif 'hospital' in self.request.path:
			return '/hospital/home/'
		else:
			return '/home/'


class UserLogoutView(LogoutView):
	template_name = "core/registration/logout.html"

	def get_redirect_url(self):
		if 'concert' in self.request.path:
			return '/concert/home/'
		elif 'plane' in self.request.path:
			return '/plane/home/'
		elif 'hospital' in self.request.path:
			return '/hospital/home/'
		else:
			return '/home/'

class UserPasswordChangeView(PasswordChangeView):
	template_name = "core/registration/password_change_form.html"

	def get_redirect_url(self):
		if 'concert' in self.request.path:
			return '/concert/password_change/done/'
		elif 'plane' in self.request.path:
			return '/plane/password_change/done/'
		elif 'hospital' in self.request.path:
			return '/hospital/password_change/done/'
		else:
			return '/password_change/done/'

class UserPasswordChangeDoneView(PasswordChangeDoneView):
	template_name = "core/registration/password_change_done.html"

class UserPasswordResetView(PasswordResetView):
	template_name = "core/registration/password_reset_form.html"
	email_template_name = "core/registration/password_reset_email.html"
	subject_template_name = "core/registration/password_reset_subject.txt"
	from_email = "no_reply@tic.com"

class UserPasswordResetDoneView(PasswordResetDoneView):
	template_name = "core/registration/password_reset_done.html"

class UserPasswordResetConfirmView(PasswordResetConfirmView):
	template_name = "core/registration/password_reset_confirm.html"

class UserPasswordResetCompleteView(PasswordResetCompleteView):
	template_name = "core/registration/password_reset_complete.html"

#########################################################
#########################################################

class UserProfileView(DetailView):
	model = UserProfile
	template_name = "core/user_profile.html"
	context_object_name = 'profile'

	def get_object(self):
		return UserProfile.objects.get(user=self.request.user)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class UserProfileEditView(FormView):
	template_name = "core/user_profile_edit.html"
	form_class = UserProfileEditForm
	success_url = 'profile'

	def form_valid(self, form):
		self.success_url = redi_url(self.request.path, self.success_url)
		first_name = form.cleaned_data.get('first_name')
		last_name = form.cleaned_data.get('last_name')
		email = form.cleaned_data.get('email')
		bio = form.cleaned_data.get('bio')
		profile_image = form.cleaned_data.get('profile_image')
		profile = UserProfile.objects.get(user=self.request.user)
		profile.user.first_name = first_name if first_name else profile.user.first_name
		profile.user.last_name = last_name if last_name else profile.user.last_name
		profile.user.email = email if email else profile.user.email
		profile.bio = bio if bio else profile.bio
		profile.profile_image = profile_image if profile_image else profile.profile_image

		profile.user.save()
		profile.save()

		return super().form_valid(form)


class UserAccountView(DetailView):
	model = UserAccount
	template_name = "core/user_account.html"
	context_object_name = 'account'

	def get_object(self):
		return UserAccount.objects.get(user=self.request.user)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class UserAccountUpdateView(FormView):
	template_name = "core/user_account_update.html"
	form_class = PaymentForm
	success_url = 'account'

	def form_valid(self, form):
		self.success_url = redi_url(self.request.path, self.success_url)
		account = UserAccount.objects.get(user=self.request.user)
		account.balance += form.cleaned_data.get('amount')
		account.save()

		return super().form_valid(form)