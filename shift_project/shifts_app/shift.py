from django.db import models
from django.db.models import Q
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from shifts_app.shift_group import ShiftGroup
#import utils.shift_creation

#models store

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        #run_times_list -> [{start_time=time, end_time=time},{...},{...}]
        from shifts_app.run import Run

        runs_to_create = []

        #can we assume shifts are never more than a day long

        shift_group = ShiftGroup.objects.all()

        if shift_group:
            #logic isnt right

            def findDuplicate(shift):

                if not (shift.start_datetime == start_datetime and shift.end_datetime == end_datetime):
                    if (shift.start_datetime.weekday() == start_datetime.weekday() and shift.end_datetime.weekday() == end_datetime.weekday() and shift.start_datetime.time() == start_datetime.time() and shift.end_datetime.time() == end_datetime.time()):
                        print('gang')
                        return True
                else:
                    print('duplicate')
                    return True
            shift_exists = filter(findDuplicate, shift_group)
            print(shift_exists)

            if shift_exists:
                print('shift exists')
                shift_exists = shift_exists[0]
                if shift_exists.start_date_range > start_datetime.date():
                    shift_group = ShiftGroup.objects.filter(start_datetime=shift_exists.start_datetime, end_datetime=shift_exists.end_datetime)
                    shift_group.update(start_date_range=start_datetime.date())
                    shift_group = shift_group[0]
                else:
                    shift_group = ShiftGroup.objects.get(start_datetime=shift_exists.start_datetime, end_datetime=shift_exists.end_datetime)
                if shift_exists.end_date_range < end_datetime.date():
                    shift_group = ShiftGroup.objects.filter(start_datetime=shift_exists.start_datetime, end_datetime=shift_exists.end_datetime)
                    shift_group.update(end_date_range=end_datetime.date())
                    shift_group = shift_group[0]
                else:
                    shift_group = ShiftGroup.objects.get(start_datetime=shift_exists.start_datetime, end_datetime=shift_exists.end_datetime)
            else:
                print('create new shift')
                shift_group = ShiftGroup.objects.create(start_datetime=start_datetime, end_datetime=end_datetime, start_date_range=start_datetime.date(), end_date_range=end_datetime.date())
        else:
            print('else hit')
            shift_group = ShiftGroup.objects.create(start_datetime=start_datetime, end_datetime=end_datetime, start_date_range=start_datetime.date(), end_date_range=end_datetime.date())

        shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group = shift_group)
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

        #lte = less than or equal to
        #gte = greater than or equal to

class Shift(models.Model):
    #runs_related
    
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    shift_group = models.ForeignKey(ShiftGroup, related_name='shift_set', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start_datetime)

    class Meta:
        app_label = "shifts_app"
        db_table="shift"
