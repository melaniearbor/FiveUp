from django import forms
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView

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


class PublicUserCreation(CreateView, ModelFormMixin):

    model = User
    template_name = 'index.html'
    form_class = FUserCreationForm
    success_url = '/signup-success/'
    fields = ['name', 'email', 'phone_number', 'carrier', 'how_many_messages', 'user_timezone', 'password']
    labels = {
        'name': _('what can we call you? Pete? Cindy?'),
        'email': _('what\'s your email address?'),
        'phone_number': _('phone number:'),
        'carrier': _('your mobile carrier'),
        'how_many_messages': _('how many fabulous messages do you want each day?'),
        'user_timezone': _('your time zone')
    }


class FiveUUserChangeForm(UpdateView):

    template_name = 'profile_change.html'
    model = User
    fields = ['phone_number', 'carrier', 'user_timezone', 'receiving_messages', 'how_many_messages']
    success_url = "/login/"

    def get_object(self):
        return User.objects.get(uuid=self.kwargs.get("uuid"))
