from django.db import models
from django.db.models import Q
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime


from shifts_app.shift_group import ShiftGroup

#models store

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        #run_times_list -> [{start_time=time, end_time=time},{...},{...}]
        from shifts_app.run import Run

        runs_to_create = []
        shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime)
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


    def get_shifts_in_datetime_range(self, start_datetime, end_datetime):
        return self.filter(
            Q(start_datetime__lte=start_datetime, end_datetime__gte=start_datetime)
            | Q(start_datetime__lte=end_datetime, end_datetime__gte=end_datetime)
            | Q(start_datetime__gte=start_datetime, end_datetime__lte=end_datetime)
            | Q(start_datetime__lte=start_datetime, end_datetime__gte=end_datetime)
        )

class Shift(models.Model):
    #runs_related
    db_table="shift"
    
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        app_label = "shifts_app"
