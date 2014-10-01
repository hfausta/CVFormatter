from django.shortcuts import render
from django.http import HttpResponse

# import account model
from registration.models import Account

# Create your views here.
def index(request):
	return render(request, 'registration/index.html')
	
def register(request):
	return HttpResponse("Registration page")
	