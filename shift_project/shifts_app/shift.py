from django.db import models
from django.utils.timezone import utc, make_aware, get_default_timezone

from shifts_app.shift_group import ShiftGroup

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        #run_times_list -> [{start_time=time, end_time=time},{...},{...}]
        from shifts_app.run import Run

        # shift_instance = self.create(start_date=start_date, end_date=end_date)
        last_end_datetime = None
        for run_times_dict in run_times_list:
            if run_times_dict['start_time'] > run_times_dict['end_time']:

            start_datetime = make_aware(start_date, run_times_dict['start_time'])
            end_datetime = make_aware(start_date, run_times_dict['end_time'])
            if start_datetime > end_datetime:
                end_datetime += timedelta(day=1)

            # Run.objects.create(
            #     shift=shift_instance,
            #     start_datetime=start_datetime,
            #     end_datetime=end_datetime
            # )
        return shift_instance


class Shift(models.Model):

    #runs_related

    db_table="shift"
    objects = ShiftManager()

    shift_group = models.ForeignKey(ShiftGroup, related_name="shifts_related")#, default=None, null=True, blank=True)

    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        app_label = "shifts_app"
