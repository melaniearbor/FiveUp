from django.shortcuts import render
from django.views.generic.edit import CreateView, ModelFormMixin
from messagebox.models import Message
from django.utils.translation import ugettext_lazy as _ 

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
    # TODO - replace base.html with something that makes sense.
    # success_url = 'add-message-success'

    # recipient = get_user()

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        def get_user_uuid():
            user_uuid=self.kwargs['uuid']
            # users = models.ForeignKey(settings.AUTH_USER_MODEL)
            # user = users.objects.get(uuid=uuid)
            return user_uuid
        Message.recipient = get_user_uuid()
        new_message = form.save(commit=False)
        new_message.save()
        self.object = new_message

        return super(ModelFormMixin, self).form_valid(form)
    
    # Message.save(self)

    # def get_success_url(self):
    #     return reverse('add-message-view')