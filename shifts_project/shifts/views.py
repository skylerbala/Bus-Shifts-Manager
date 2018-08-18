from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse_lazy
from .models import Shift, Run, ShiftGroup
from .forms import ShiftForm, SelectNumberOfRunsForm, RunForm, EmployeeForm
import datetime
from string import join


template_name = 'shifts/index.html'
# Shifts
@user_passes_test(lambda u:u.is_staff, login_url=reverse_lazy('shifts:forbidden'))
def get_shifts(request):
    if request.method == 'GET':
        all_shifts = Shift.objects.all()
        shift_form = ShiftForm()
        employee_form = EmployeeForm()
        select_number_of_runs_form = SelectNumberOfRunsForm()
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1 

        data = {
            'shift_form': shift_form,
            'employee_form': employee_form,
            'all_shifts': all_shifts,
            'select_number_of_runs_form': select_number_of_runs_form
        }
        return render(request, template_name, data)

def add_shift(request):
    if request.method == 'POST':
        response = {}

        shift_form = ShiftForm(request.POST)
        employee_form = EmployeeForm(request.POST)

        shift_groups = ShiftGroup.objects.get_ordered_shift_groups()
        run_times_list = []
        if shift_form.is_valid() and employee_form.is_valid():
            start_datetime = shift_form.cleaned_data['start_datetime']
            end_datetime = shift_form.cleaned_data['end_datetime']
            employee = employee_form.cleaned_data['employee']

            for i in range(0, int(request.POST['number_of_runs'])):
                start_datetime_val = 'start_datetime_run_' + str(i)
                end_datetime_val = 'end_datetime_run_' + str(i)
                line_val = 'run_line' + str(i)
                run_start_datetime = datetime.datetime.strptime((request.POST[start_datetime_val]), "%m/%d/%Y %H:%M").time()
                run_end_datetime = datetime.datetime.strptime((request.POST[end_datetime_val]), "%m/%d/%Y %H:%M").time()
                run_line = request.POST[line_val]

                run_times_list.append({
                    'start_time': run_start_datetime,
                    'end_time': run_end_datetime,
                    'line': run_line
                })

            shift_instance = Shift.objects.create_shift(start_datetime, end_datetime, run_times_list, employee)

            lines = []
            for run in shift_instance.run_set.all():
                lines += run.line
            lines = ', '.join(lines)
            
            response = {
                'shiftID': shift_instance.id,
                'coverage': shift_instance.employee or 'Open',
                'lines': lines,
                'date': shift_instance.start_datetime.strftime('%m/%d/%y'),
                'day': shift_instance.start_datetime.strftime('%A'),
                'startTime': shift_instance.start_datetime.strftime('%H:%M'),
                'endTime': shift_instance.end_datetime.strftime('%H:%M'),
            }

            return JsonResponse(response)

def update_shift(request, pk):
    pass

def delete_shift(request, pk):
    Shift.objects.delete_shift(pk=pk)
    return redirect('shifts:index')

def forbidden(request):
    return render(request, 'shifts/403.html')


