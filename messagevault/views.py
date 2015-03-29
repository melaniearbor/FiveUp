from django.shortcuts import render
from messagevault.models import CuratedMessage
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext as _

# Create your views here.
class CuratedMessageForm(ModelForm):

    model = CuratedMessage
    fields = ['message_text', 'message_author_first', 'message_author_last']
    labels = {
        'message_text': _('Message text:'),
        'message_author_first': _("Author's first name:"),
        'message_author_last': _("Author's last name:")
    }

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        new_message = form.save(commit=False)
        final_message_str = message_text + " -" + message_author_first + " " + message_author_last
        total_characters = len(final_message_str)
        if total_characters > 160:
            raise ValidationError('The total characters exceed 160; shorten the message.')
        else:
            new_message.save()
        self.object = new_message

        return super(ModelForm, self).form_valid(form)