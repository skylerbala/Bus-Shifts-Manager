from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from django.db import models
from django.db.models import Q

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        from .shift_groups import ShiftGroup
        from .runs import Run

        runs_to_create = []
        shift_group = ShiftGroup.objects.get_or_create(start_datetime=start_datetime, end_datetime=end_datetime)

        shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=shift_group)
        last_end_date = start_datetime.date()

        for run_times_dict in run_times_list:
            run_start_datetime = make_aware( datetime.datetime.combine(last_end_date, run_times_dict['start_time']), get_default_timezone() ).astimezone(utc)
            run_end_datetime = make_aware(datetime.datetime.combine(last_end_date, run_times_dict['end_time']), get_default_timezone()).astimezone(utc)
            if run_start_datetime > run_end_datetime:
                run_end_datetime += datetime.timedelta(days=1)
            last_end_date = run_end_datetime.date()

            runs_to_create.append(Run(
                shift=shift_instance,
                start_datetime=run_start_datetime,
                end_datetime=run_end_datetime
            ))
        Run.objects.bulk_create(runs_to_create)

        return shift_instance

class Shift(models.Model):    
    from .shift_groups import ShiftGroup
    
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    shift_group = models.ForeignKey(ShiftGroup, related_name='shift_set', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.start_datetime)

    def get_absolute_url(self):
        return str(self.start_datetime)

    class Meta:
        app_label = "shifts_app"
        db_table="shift"
