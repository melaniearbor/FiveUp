from django.shortcuts import render
from django.views.generic.edit import CreateView
from messagebox.models import Message
from django.utils.translation import ugettext_lazy as _ 

# Create your views here.

class CreateMessageView(CreateView):

    def get_user(self):
        uuid=self.kwargs['uuid']
        users = models.ForeignKey(settings.AUTH_USER_MODEL)
        user = users.objects.get(uuid=uuid)
        return user
        # TODO fetch user profile based on uuid & return user

    model = Message
    template_name = 'add_message.html'
    fields = ['sender_name', 'message_text']
    labels = {
        'sender_name': _('Your name:'),
        'message_text': _('Your message:'),
    }
    #recipient = self.get_user

    def get_success_url(self):
        return reverse('message-list')