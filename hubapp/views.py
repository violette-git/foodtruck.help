from urllib import request
from django.shortcuts import render, redirect
from django.template import engines
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
import requests
import html
from user_app.views import User

# Create your views here.


def test(request):

	return render(request, 'hubapp/test.html') 


def display(request):

    context = {


    }
    return render(request, 'hubapp/display.html', context)

def controller(request):

    context = {

    }

    return render(request, 'hubapp/controller.html', context)

def whereami(request):
	# if request.method == 'GET':
		
	url = "https://www.google.com/maps/dir/?api=1"
	payload = ""
	headers = {
	}
	
	# url2 = "https://www.google.com/recaptcha/api/siteverify"


	response = requests.request("GET", url, headers=headers, data=payload)
	# print(response.text)
	html = response.text
	# print(html)
	django_engine = engines['django']
	template = django_engine.from_string(html)
	# test = lxml.html.fromstring(f'{html}')
	# print(template.render(), 'templates', '----------------------------------------------')
	new_template = template.render()
	context = {
		'stuff': new_template
	}
	# template.render(context)
	# return render(request, 'hubapp/whereami.html', context)
	return HttpResponseRedirect(url)



class Home(TemplateView):
    
    template_name = "home.html"
    xtra_context={'all_fields': User._meta.get_fields()}

# class SettingsView(LoginRequiredMixin, TemplateView):
#     def get(self, request, *args, **kwargs):
#         user = request.user

#         try:
#             github_login = user.social_auth.get(provider='github')
#         except UserSocialAuth.DoesNotExist:
#             github_login = None

#         try:
#             twitter_login = user.social_auth.get(provider='twitter')
#         except UserSocialAuth.DoesNotExist:
#             twitter_login = None

#         try:
#             facebook_login = user.social_auth.get(provider='facebook')
#         except UserSocialAuth.DoesNotExist:
#             facebook_login = None

#         can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

#         return render(request, 'core/settings.html', {
#             'github_login': github_login,
#             'twitter_login': twitter_login,
#             'facebook_login': facebook_login,
#             'can_disconnect': can_disconnect
#         })


# @login_required
# def password(request):
#     if request.user.has_usable_password():
#         PasswordForm = PasswordChangeForm
#     else:
#         PasswordForm = AdminPasswordChangeForm

#     if request.method == 'POST':
#         form = PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordForm(request.user)
#     return render(request, 'core/password.html', {'form': form})