from django.db import models
import datetime

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