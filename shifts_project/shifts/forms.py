from django.utils.translation import gettext_lazy as _
from django import forms
from .models.shifts import Shift
from .models.runs import Run
from employees.models import Employee

import datetime

class EmployeeChoiceField(forms.ModelChoiceField):
  def label_from_instance(self, obj):
    print(obj)
    return "{}; {}".format(obj.user.first_name, obj.user_id)

class EmployeeForm(forms.Form):
  employee = EmployeeChoiceField(queryset=Employee.objects.all(), label='Employee Name/ID', required=False)

class ShiftForm(forms.Form):
  start_datetime = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='Start', help_text='Enter start date/time')
  end_datetime = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'],widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='End', help_text='Enter end date/time')
  
class RunForm(forms.Form):
  start_datetime = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='Start')
  end_datetime = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'],widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='End')

class SelectNumberOfRunsForm(forms.Form):
  CHOICES = [ (i,i) for i in range(11) ]
  number_of_runs = forms.ChoiceField(choices=CHOICES, label='Runs')

  def __str__(self):
    return 'Runs: {}' % (self.number_of_runs)
