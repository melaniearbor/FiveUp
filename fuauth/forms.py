from django import forms
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from fuauth.models import User


class FUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "phone_number",
            "carrier",
            "user_timezone",
            "password",
        ]

    def save(self, commit=True):
        user = super(FUserCreationForm, self).save(commit=False)
        user.set_password(user.password)
        user.is_active = True
        if commit:
            user.save()
        return user


class AdminUserCreationForm(FUserCreationForm):
    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "phone_number",
            "carrier",
            "user_timezone",
            "password",
            "is_staff",
            "is_active",
            "receive_newsletter",
        ]


class PublicUserCreation(CreateView, ModelFormMixin):

    model = User
    template_name = "index.html"
    form_class = FUserCreationForm
    success_url = "/"
    fields = [
        "name",
        "email",
        "phone_number",
        "carrier",
        "how_many_messages",
        "user_timezone",
        "password",
    ]
    labels = {
        "name": _("what can we call you? Pete? Cindy?"),
        "email": _("what's your email address?"),
        "phone_number": _("phone number:"),
        "carrier": _("your mobile carrier"),
        "how_many_messages": _("how many fabulous messages do you want each day?"),
        "user_timezone": _("your time zone"),
    }


class FiveUUserChangeForm(UpdateView):

    template_name = "profile_change.html"
    model = User
    fields = [
        "phone_number",
        "carrier",
        "user_timezone",
        "receiving_messages",
        "how_many_messages",
    ]
    success_url = "/login/"

    # def get(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated():
    #         return redirect("/login/")
    #     elif str(request.user.uuid) != self.kwargs.get("uuid"):
    #         return redirect("/login/")
    #     else:
    #         return super(FiveUUserChangeForm, self).get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect("/login/")
        elif str(request.user.uuid) != self.kwargs.get("uuid"):
            return redirect("/login/")
        else:
            return super(FiveUUserChangeForm, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return User.objects.get(uuid=self.kwargs.get("uuid"))
