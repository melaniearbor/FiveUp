from django.forms import ModelForm
from django.utils.translation import ugettext as _
from messagevault.models import CuratedMessage


class CuratedMessageForm(ModelForm):

    model = CuratedMessage
    fields = ["message_text", "message_author_first", "message_author_last"]
    labels = {
        "message_text": _("Message text:"),
        "message_author_first": _("Author's first name:"),
        "message_author_last": _("Author's last name:"),
    }
