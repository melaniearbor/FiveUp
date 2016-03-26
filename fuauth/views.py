from django.shortcuts import render, render_to_response, redirect 
from django.contrib.auth import views
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from fuauth.forms import FUserCreationForm
from fuauth.models import User

# Create your views here.

def success(request):
    # context = {'user_uuid': user_uuid}
    template_name = 'registration/login.html'
    return render(request, template_name)

def testsign(request):
	template_name = 'sign_up.html'
	return render(request, template_name)

def register(request):
    context = RequestContext(request) #where is RequestContext defined

    registered = False

    def send_confirmation_text(now_phone, now_carrier):
        message = "Hey there, partner! Hold on to your hat, because you're about to get lots of happy. Starting tomorrow. Doodle-oodle-oo. Wah wah wah."
        msg_to = now_phone + '@' + now_carrier
        mail = EmailMultiAlternatives(
          subject="FiveUp",
          body=message,
          from_email="Five Up <app44043297@heroku.com>",
          to=[msg_to],
        )
        mail.send()

    if request.method == 'POST':
        user_form = FUserCreationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            registered = True
            authenticated_user = authenticate(username=request.POST['email'],password=request.POST['password'])
            login(request, authenticated_user)
            now_phone = request.POST['phone_number']
            now_carrier = request.POST['carrier']
            send_confirmation_text(now_phone, now_carrier)

        else:
            print(user_form.errors)
    else:
        user_form = FUserCreationForm()

    return render_to_response(
            'registration/login.html',
            {'user_form': user_form, 'registered': registered},
            context)

def loginform(request):
    template_name = 'loginform.html'
    return render(request, template_name)

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect('/home/')
    return render_to_response('registration/login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return render_to_response('registration/logout.html', context_instance=RequestContext(request))


