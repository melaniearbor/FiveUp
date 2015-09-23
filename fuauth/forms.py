from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _ 
from django.views.generic.edit import CreateView, ModelFormMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings


from fuauth.models import User


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_form"] = AuthenticationForm()
        return context




