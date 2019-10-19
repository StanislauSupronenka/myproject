from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login


# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

from users.forms import RegistrationForm
from users.models import Siteuser


def start_page(request):
    return render(request,'main_login_form.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, "main_login_form.html", context={
            "error": False
        })
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/rates')
    else:
        try:
            user = Siteuser.objects.get(username=username)
            user.incorrect_attempts += 1
            if user.incorrect_attempts > settings.INCORRECT_ATTEMPTS_LIMIT:
                user.is_active = False
            user.save()
        except Siteuser.DoesNotExist:
            pass
        return render(request, "main_login_form.html", context={
            "error": True
        })


def logout_view(request):
    logout(request)
    return redirect('/')

@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/rates')
    else:
        form = RegistrationForm()
    return render(request, "registration.html", context={
        "form": form
    })


