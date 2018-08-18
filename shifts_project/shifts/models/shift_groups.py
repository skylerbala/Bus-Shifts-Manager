from django.db import models
import datetime

class ShiftGroupManager(models.Manager):        

    def get_or_create(self, start_datetime, end_datetime):
        shift_group = None

        try:
            weekday = (1 + start_datetime.weekday()) % 7 + 1

            shift_group = self.get(start_datetime__week_day=weekday, start_datetime__hour=start_datetime.hour, start_datetime__minute=start_datetime.minute, end_datetime__week_day=weekday, end_datetime__hour=end_datetime.hour, end_datetime__minute=end_datetime.minute)

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
    
    def get_ordered_shift_groups(self):
        from .shifts import Shift
        def add_shifts(sg):
            shifts = Shift.objects.filter(shift_group_id=sg['id']).order_by('start_datetime')
            sg['shifts'] = shifts
            return sg
        def sortByWeekday(shift_group):
            return shift_group['start_datetime'].weekday()

        shift_groups = ShiftGroup.objects.all().values()
        shift_groups = map(add_shifts, shift_groups)
        shift_groups = sorted(shift_groups, key=sortByWeekday)

        return shift_groups


class ShiftGroup(models.Model):
    objects = ShiftGroupManager()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()