from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .views import (HomeView, CustomerRegistrationView, ContentCreatorRegistrationView, UserLoginView, 
					UserLogoutView, UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView,
					UserPasswordResetCompleteView, UserPasswordChangeView, UserPasswordChangeDoneView, UserProfileView,
					UserProfileEditView, UserAccountView, UserAccountUpdateView
					)

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('register/', CustomerRegistrationView.as_view(), name='customer_create'),
    path('ccregister/', ContentCreatorRegistrationView.as_view(), name='content_creator_create'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', UserPasswordChangeDoneView.as_view(), name='password_change_done'),    
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),    
    path('reset/done/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('403/', TemplateView.as_view(template_name='core/errors/403.html'), name='error_403'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/edit/', UserProfileEditView.as_view(), name='user_profile_edit'),
    path('account/', UserAccountView.as_view(), name='user_account'),
    path('account/update/', UserAccountUpdateView.as_view(), name='user_account_update'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
