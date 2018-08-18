from django.shortcuts import render
from django.http import JsonResponse
from shifts.models.shifts import Shift

def market(request):
    if request.method == 'GET':
        uncovered_shifts = Shift.objects.get_uncovered_shifts(request)
        data = {
            'uncovered_shifts': uncovered_shifts
        }

        return render(request, 'market/index.html', data)

def market_cover(request, pk):
    shift = Shift.objects.get(pk=pk)
    if request.is_ajax():
        data = {
            'shift-filled': False
        }
        if not shift.employee == None:
            data['shift-filled'] = True
            return JsonResponse(data)

        shift.employee = request.user.employee
        shift.save()
        
        return JsonResponse(data)
    else:
        uncovered_shifts = Shift.objects.get_uncovered_shifts(request)
        data = {
            'uncovered_shifts': uncovered_shifts,
            'shift_filled': False
        }
        
        if not shift.employee == None:
            data['shift_filled'] = True
            return render(request,'market/index.html', data)

        shift.employee = request.user.employee
        shift.save()
        return render(request,'market/index.html', data)