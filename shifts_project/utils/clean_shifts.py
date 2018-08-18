from shifts.models import *

def clean_shifts_now():
  all_shifts = Shift.objects.all()
  all_shift_groups = ShiftGroup.objects.all()

  for shift in all_shifts:
    if shift.end_datetime.time <= shift.start_datetime.time:
      shift.delete()
    for run in shift.run_set.all():
      if run.start_datetime < shift.start_datetime or run.end_datetime > shift.end_datetime:
        run.delete()
    if not shift.run_set.all().exists():
      shift.delete()

  for sg in all_shift_groups:
    if not sg.shift_set.all().exists():
      sg.delete()
    if sg.end_datetime.time <= sg.start_datetime.time:
      sg.delete()

