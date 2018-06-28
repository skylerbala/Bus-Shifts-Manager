from django.db import models
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from django.db.models import Q

class ShiftGroupManager(models.Manager):        

    def get_or_create(self, start_datetime, end_datetime):
        shift_group = None

        try:
            weekday = (1 + start_datetime.weekday()) % 7 + 1

            shift_group = self.get(start_datetime__week_day=weekday, start_datetime__hour=start_datetime.hour, start_datetime__minute=start_datetime.minute)

            print('get existing shift')
            if shift_group.start_datetime.date() > start_datetime.date():
                shift_group.start_datetime=start_datetime
            if shift_group.end_datetime.date() < end_datetime.date():
                shift_group.end_datetime=end_datetime
            shift_group.save()

        except ShiftGroup.DoesNotExist:
            print('create new shift')
            shift_group = self.create(start_datetime=start_datetime, end_datetime=end_datetime)

        return shift_group


class ShiftGroup(models.Model):
    objects = ShiftGroupManager()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        app_label = "shifts_app"
        db_table = "shift_groups"


        '''
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
        '''