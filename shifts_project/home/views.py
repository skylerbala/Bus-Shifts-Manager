from django.shortcuts import render
from django.views import generic
from shifts.models import *

class HomeView(generic.View):
  template_name = 'home/index.html'
   
  def get(self, request):
    all_shifts = Shift.objects.all()
    shift_groups =  ShiftGroup.objects.all()
    uncovered_shifts = Shift.objects.get_uncovered_shifts(request)
    my_shifts = Shift.objects.filter(employee__exact=request.user.employee).order_by('start_datetime')
    return render(request, self.template_name, {
      'all_shifts': all_shifts,
      'shift_groups': shift_groups,
      'uncovered_shifts': uncovered_shifts,
      'my_shifts': my_shifts,
    })