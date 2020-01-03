from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView, ModelFormMixin
from fuauth.models import User
from messagebox.models import Message


class CreateMessageView(CreateView, ModelFormMixin):

    model = Message
    template_name = "add_message.html"
    fields = ["sender_name", "message_text"]
    labels = {"sender_name": _("Your name:"), "message_text": _("Your message:")}

    def recipient(self, **kwargs):
        recipient_uuid = self.kwargs["uuid"]
        try:
            return User.objects.get(uuid=recipient_uuid)
        except ObjectDoesNotExist:
            return redirect("/")

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        new_message = form.save(commit=False)
        recipient_uuid = self.kwargs["uuid"]
        try:
            new_message.recipient = User.objects.get(uuid=recipient_uuid)
        except ObjectDoesNotExist:
            return redirect("/")
        new_message.save()
        self.object = new_message

        return super(ModelFormMixin, self).form_valid(form)


def success(request):
    template_name = "message_add_success.html"
    return render(request, template_name)


def contact(request):
    template_name = "contact.html"
    return render(request, template_name)
