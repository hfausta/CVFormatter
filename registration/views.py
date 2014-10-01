from django.shortcuts import render
from django.http import HttpResponse

# import account model
from .models import Account

# import registration form
from .form import RegistrationForm

# Create your views here.
def index(request):
	return render(request, 'registration/index.html')
	
def register(request):
	# declare registration form
	registration_form = RegistrationForm()
	
	# context will be passed to the template page
	context = { "registration_form" : registration_form }
	
	# the template page that will be displayed
	template = 'registration/register.html'
	
	return render(request, template, context)
