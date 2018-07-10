from django.utils.translation import gettext_lazy as _
from django import forms
from .models.shifts import Shift
from .models.runs import Run

import datetime

class ShiftForm(forms.Form):
  start_datetime = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='Start', help_text='Enter start date/time')
  end_datetime = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='End', help_text='Enter end date/time')

class RunForm(forms.Form):
  start_datetime = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='Start', help_text='Enter start date/time')
  end_datetime = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.DateTimeInput(attrs={'class':'form-control col-form-label', 'data-toggle':'datepicker'}), label='End', help_text='Enter end date/time')

class SelectNumberOfRunsForm(forms.Form):
  CHOICES = [ (i,i) for i in range(10) ]
  number_of_runs = forms.ChoiceField(choices=CHOICES, label='Runs')

