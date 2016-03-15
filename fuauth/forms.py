from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _ 
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.contrib.auth.decorators import login_required

from fuauth.models import User
from courier.models import UserSendTime


class FUserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 'password', 
        'is_staff', 'is_active', 'receive_newsletter']


    def save(self, commit=True):
        user = super(FUserCreationForm, self).save(commit=False)
        user.set_password(user.password)
        user.is_active = True
        print('I am neat!')
        if commit:
            user.save()
        return user

class PublicUserCreation(CreateView, ModelFormMixin): #AjaxTemplateMixin

    model = User
    template_name = 'index.html'
    form_class = FUserCreationForm
    success_url = '/signup-success/'
    fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 'password']
    labels = {
        'name': _('what can we call you? Pete? Cindy?'),
        'email': _('what\'s your email address?'),
        'phone_number': _('phone number:'), 
        'carrier': _('your mobile carrier'),
        'user_timezone': _('your time zone')
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["login_form"] = AuthenticationForm()
    #     return context

class FiveUUserChangeForm(UpdateView):

    template_name = 'profile_change.html'
    model = User
    fields = ['phone_number', 'carrier', 'user_timezone', "receiving_messages"]
    success_url = "/login/"


    def get_object(self):
        return User.objects.get(uuid=self.kwargs.get("uuid"))





