from django.shortcuts import render
from django.views.generic.edit import CreateView, ModelFormMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models


from fuauth.models import User
from fuauth.forms import PublicUserCreation
from messagebox.models import Message


class CreateMessageView(CreateView, ModelFormMixin):

    model = Message
    template_name = 'add_message.html'
    fields = ['sender_name', 'message_text']
    labels = {
        'sender_name': _('Your name:'),
        'message_text': _('Your message:'),
    }

    def recipient(self, **kwargs):
        recipient_uuid = self.kwargs['uuid']
        recipient = User.objects.get(uuid=recipient_uuid)
        return recipient

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        def get_user():
            user_uuid = self.kwargs['uuid']
            user = User.objects.get(uuid=user_uuid)
            return user
        new_message = form.save(commit=False)
        new_message.recipient = get_user()
        new_message.save()
        self.object = new_message

        return super(ModelFormMixin, self).form_valid(form)


def success(request):
    template_name = 'message_add_success.html'
    return render(request, template_name)


def index(request):
    context = {'form': form}
    template_name = 'index.html'
    return render(request, template_name)


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)
