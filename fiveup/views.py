import os

from django.contrib.staticfiles import finders
from django.http import HttpResponse


def display_cert(request):
    file_path = finders.find("BA7CD11C05866445FBFE053E2C1AAA8C.txt")

    with open(file_path, "rb") as txt_file:
        response = HttpResponse(txt_file.read(), content_type="text/plain")
        response["Content-Disposition"] = "inline; filename=" + os.path.basename(
            file_path
        )
        return response
