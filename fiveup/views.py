import os
from django.conf import settings
from django.http import HttpResponse


def display_cert(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'BA7CD11C05866445FBFE053E2C1AAA8C.txt')
    with open(file_path, 'rb') as txt_file:
        response = HttpResponse(txt_file.read(), content_type="text/plain")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
