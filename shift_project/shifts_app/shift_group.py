from django.db import models
from shifts_app.shift import Shift
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime

class ShiftGroupManager(models.Manager):
    pass


class ShiftGroup(models.Model):

    #shifts_related = 
    
    objects = ShiftGroupManager()

    def get_shifts(self):
        start_datetime = make_aware(datetime.datetime(2017,5,1), get_default_timezone())
        end_datetime = make_aware(datetime.datetime(2017,5,3), get_default_timezone())
        return Shift.objects.get_shifts_in_datetime_range(start_datetime, end_datetime)




    class Meta:
        app_label = "shifts_app"
        db_table = "shift_group"