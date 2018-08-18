from django.shortcuts import render, HttpResponse
from shifts.models.shifts import Shift

# My Shifts
def my_shifts(request):
  if request.method == 'GET':
      my_shifts = Shift.objects.filter(employee__exact=request.user.employee).order_by('start_datetime')

      data = {
          'my_shifts': my_shifts,
      }

      return render(request, 'my_shifts/index.html', data)

def my_shifts_post(request, pk):
    my_shift = Shift.objects.get(pk=pk)
    my_shift.employee = None
    my_shift.save()
    return HttpResponse("Success")