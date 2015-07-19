from django.shortcuts import render
from django.contrib.auth import views

# Create your views here.

def success(request):
    # context = {'user_uuid': user_uuid}
    template_name = 'registration/login.html'
    return render(request, template_name)

def testsign(request):
	template_name = 'sign_up.html'
	return render(request, template_name)

