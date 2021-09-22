from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=form.cleaned_data['username'],

                                password=form.cleaned_data['password1'],
                                )
            login(request, user)
            form.save()
            return render(request, "account_pages/home.html", {})
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})

