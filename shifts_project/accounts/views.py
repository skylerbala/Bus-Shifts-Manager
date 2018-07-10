from django.shortcuts import render, redirect, render
from django.core.urlresolvers import reverse
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout

# Create your views here.

def register(request):
  form = RegistrationForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect(reverse('accounts:login'))

  data = {'form': form}
  return render(request, 'accounts/register.html', data)

def logout(request):
  auth_logout(request)
  return redirect(reverse('accounts:login'))


def login_redirect(request):
    return redirect(reverse('accounts:login'))
