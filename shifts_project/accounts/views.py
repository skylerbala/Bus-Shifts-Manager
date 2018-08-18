from django.shortcuts import render, redirect, render, HttpResponse
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

def profile(request):
  return render(request, 'accounts/profile.html')

def update_profile(request):
  new_val = request.POST['new_val']
  new_type = request.POST['type']
  def update_call_offs():
    request.user.employee.call_offs = new_val
    request.user.employee.save()
  def update_wage():
    request.user.employee.wage = new_val
    request.user.employee.save()
  def update_first_name():
    request.user.first_name = new_val
    request.user.save()
  def update_last_name():
    request.user.last_name = new_val
    request.user.save()
  def update_phone():
    request.user.employee.phone = new_val
    request.user.employee.save()
  options = {
    'call_offs': (lambda: update_call_offs()), 
    'wage': (lambda: update_wage()), 
    'first_name': (lambda: update_first_name()), 
    'last_name': (lambda: update_last_name()), 
    'phone': (lambda: update_phone())
  }

  options[new_type]()
  return HttpResponse(new_val)