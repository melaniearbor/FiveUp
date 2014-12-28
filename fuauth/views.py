from django.shortcuts import render

# Create your views here.

def success(request):
    template_name = 'sign_up_success.html'
    return render(request, template_name)
