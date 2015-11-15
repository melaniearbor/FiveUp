from django.shortcuts import render, render_to_response, redirect 
from django.contrib.auth import views
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from fuauth.forms import FUserCreationForm

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

    if request.method == 'POST':
        user_form = FUserCreationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            # user.save()
            registered = True
            authenticated_user = authenticate(username=request.POST['email'],password=request.POST['password'])
            login(request, authenticated_user)

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


