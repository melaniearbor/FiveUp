from django.shortcuts import render
from django.views.generic.edit import CreateView, ModelFormMixin
from messagebox.models import Message
from django.utils.translation import ugettext_lazy as _ 
from django.db import models
from fuauth.models import User

# Create your views here.

class CreateMessageView(CreateView, ModelFormMixin):

    # def get_user():
    #     uuid=self.kwargs['uuid']
    #     users = models.ForeignKey(settings.AUTH_USER_MODEL)
    #     user = users.objects.get(uuid=uuid)
    #     return user
        # TODO fetch user profile based on uuid & return user

    model = Message
    template_name = 'add_message.html'
    fields = ['sender_name', 'message_text']
    labels = {
        'sender_name': _('Your name:'),
        'message_text': _('Your message:'),
    }

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        def get_user():
            user_uuid=self.kwargs['uuid']
            # users = models.ForeignKey('fuauth.User')
            user = User.objects.get(uuid=user_uuid)
            # print(user_uuid)
            return user
        new_message = form.save(commit=False)
        new_message.recipient = get_user()
        new_message.save()
        self.object = new_message

        return super(ModelFormMixin, self).form_valid(form)


def success(request):
    template_name = 'message_add_success.html'
    return render(request, template_name)
    
    # Message.save(self)

    # def get_success_url(self):
    #     return reverse('add-message-view')

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def dummy(request):
    template_name = 'dumyhome.html'
    return render(request, template_name)