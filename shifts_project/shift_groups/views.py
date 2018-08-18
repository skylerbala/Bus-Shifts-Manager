from django.shortcuts import render
from shifts.models.shift_groups import ShiftGroup
# Create your views here.
def shift_groups(request):
  if request.method == 'GET':
    shift_groups = ShiftGroup.objects.get_ordered_shift_groups()

    data = {
      'shift_groups': shift_groups,
    }
    return render(request, 'shift_groups/index.html', data)