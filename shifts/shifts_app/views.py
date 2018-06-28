from collections import OrderedDict
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from .models import Shift
from .models import ShiftGroup


class HomeView(generic.ListView):
    template_name = 'shift_app/index.html'

    def get_queryset(self):
        pass

def shifts(request):
    def add_shifts(sg):
        shifts = Shift.objects.filter(shift_group_id=sg['id']).order_by('start_datetime')
        sg['shifts'] = shifts
        return sg
    def sortByWeekday(shift_group):
        return shift_group['start_datetime'].weekday()
    
    shift_groups = ShiftGroup.objects.all().values()
    shift_groups = map(add_shifts, shift_groups)
    shift_groups = sorted(shift_groups, key=sortByWeekday)


    return render(request, 'shift_app/shift_group.html', {
        "shift_groups": shift_groups
    })
    
class ShiftCreate(CreateView):
    model = Shift
    fields = ['start_datetime', 'end_datetime']



#