from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .shift import Shift
from .shift_group import ShiftGroup
from django.core import serializers


class HomeView(generic.ListView):
    template_name = 'shift_app/index.html'

    def get_queryset(self):
        pass

def shifts(request):
    all_shift_groups = ShiftGroup.objects.all()

    def createObj(sg):
        shifts = Shift.objects.filter(shift_group_id=sg.id)
        sg.shifts = shifts
        return sg

    shift_groups = map(createObj, all_shift_groups)

    return render(request, 'shift_app/shift_group.html', {
        "shift_groups": shift_groups
    })