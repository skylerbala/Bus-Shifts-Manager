from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.decorators.http import require_GET, require_POST
from django.forms import formset_factory
from .models import Shift
from .models import Run
from .models import ShiftGroup
from .forms import ShiftForm, SelectNumberOfRunsForm, RunForm, EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import datetime


template_name = 'shifts/index.html'

def get_shifts(request):
    if request.method == 'GET':
        shift_form = ShiftForm()
        run_form = RunForm()
        employee_form = EmployeeForm()
        select_number_of_runs_form = SelectNumberOfRunsForm()
        shift_groups = get_ordered_shift_groups()

        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits+1
        print(num_visits)

        data = {
            'shift_form': shift_form,
            'run_form': run_form,
            'employee_form': employee_form,
            'shift_groups': shift_groups,
            'select_number_of_runs_form': select_number_of_runs_form
        }
        return render(request, template_name, data)

def get_num_of_runs(request):
    num_of_runs = int(request.GET['num_of_runs'])
    RunFormSet = formset_factory(RunForm, extra=num_of_runs)
    run_formset = RunFormSet()
    data = {
        'run_formset': run_formset.as_table()
    }
    return JsonResponse(data)

def add_shift(request):
    if request.method == 'POST':
        shift_form = ShiftForm(request.POST)
        shift_groups = get_ordered_shift_groups()
        select_number_of_runs_form = SelectNumberOfRunsForm()

        if shift_form.is_valid():
            start_datetime = shift_form.cleaned_data['start_datetime']
            end_datetime = shift_form.cleaned_data['end_datetime']

            run_times_list = []

            for i in range(0, int(request.POST['number_of_runs'])):
                start_datetime_val = 'start_datetime_run_' + str(i)
                end_datetime_val = 'end_datetime_run_' + str(i)

                run_start_datetime = datetime.datetime.strptime((request.POST[start_datetime_val]), "%Y/%m/%d %H:%M").time()
                run_end_datetime = datetime.datetime.strptime((request.POST[end_datetime_val]), "%Y/%m/%d %H:%M").time()

                run_times_list.append(
                    {
                        'start_time': run_start_datetime,
                        'end_time': run_end_datetime
                    }
                )

            shift_instance = Shift.objects.create_shift(start_datetime, end_datetime, run_times_list)

            return redirect('shifts:index')

        data = {
            'shift_form': shift_form, 
            'shift_groups': shift_groups,
            'select_number_of_runs_form': select_number_of_runs_form,
        }
        return render(request, template_name, data)

def update_shift(request, pk):
    pass

def delete_shift(request, pk):
    Shift.objects.delete_shift(pk=pk)
    return redirect('shifts:index')

def get_ordered_shift_groups():
    def add_shifts(sg):
        shifts = Shift.objects.filter(shift_group_id=sg['id']).order_by('start_datetime')
        sg['shifts'] = shifts
        return sg
    def sortByWeekday(shift_group):
        return shift_group['start_datetime'].weekday()

    shift_groups = ShiftGroup.objects.all().values()
    shift_groups = map(add_shifts, shift_groups)
    shift_groups = sorted(shift_groups, key=sortByWeekday)

    return shift_groups

def coverage(request):
    if request.method == 'GET':
        open_shifts = Shift.objects.filter(employee__isnull=True).order_by('start_datetime')
        filled_shifts = Shift.objects.filter(employee__isnull=False, employee__exact=request.user.employee).order_by('start_datetime')

        data = {
            'open_shifts': open_shifts,
            'filled_shifts': filled_shifts
        }

        return render(request, 'shift-coverage/index.html', data)

def coverage_fill(request, pk):
    if request.method == 'POST':
        shift = Shift.objects.get(pk=pk)
        shift.employee = request.user.employee
        shift.save()

        return redirect('shifts:coverage')