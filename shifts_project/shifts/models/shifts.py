from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Q


class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list, employee):
        from .shift_groups import ShiftGroup
        from .runs import Run

        runs_to_create = []
        shift_group = ShiftGroup.objects.get_or_create(start_datetime=start_datetime, end_datetime=end_datetime)

        shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=shift_group, employee=employee)
        last_end_date = start_datetime.date()

        for run_times_dict in run_times_list:
            run_start_datetime = make_aware( datetime.datetime.combine(last_end_date, run_times_dict['start_time']), get_default_timezone() ).astimezone(utc)
            run_end_datetime = make_aware(datetime.datetime.combine(last_end_date, run_times_dict['end_time']), get_default_timezone()).astimezone(utc)
            if run_start_datetime > run_end_datetime:
                run_end_datetime += datetime.timedelta(days=1)
            last_end_date = run_end_datetime.date()

            run_line = run_times_dict['line']

            runs_to_create.append(Run(
                shift=shift_instance,
                start_datetime=run_start_datetime,
                end_datetime=run_end_datetime,
                line=run_line
            ))
        Run.objects.bulk_create(runs_to_create)

        return shift_instance

    def delete_shift(self, pk):
        from .shift_groups import ShiftGroup

        shift_delete = Shift.objects.get(pk=pk)
        shift_group_id = shift_delete.shift_group.pk
        shifts_count = Shift.objects.filter(shift_group_id=shift_group_id).count()

        if shifts_count == 1:
            ShiftGroup.objects.filter(pk=shift_group_id).delete()
        
        shift_delete.delete()
    
    def get_uncovered_shifts(self, request):
        return Shift.objects.filter(Q(employee__isnull=True)).exclude(employee__exact=request.user.employee).order_by('start_datetime')


class Shift(models.Model):    
    from .shift_groups import ShiftGroup
    from employees.models import Employee
    
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    shift_group = models.ForeignKey(ShiftGroup, related_name='shift_set', on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, related_name='shift_set', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.start_datetime)

    def get_absolute_url(self):
        return reverse('shift-detail', kwargs={
            'pk': self.pk
        })

