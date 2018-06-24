from django.db import models
from shifts_app.shift import Shift
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime

class ShiftGroupManager(models.Manager):
    pass


class ShiftGroup(models.Model):

    #shifts_related = 
    
    objects = ShiftGroupManager()
    date = models.DateField()


    def get_shifts(self):
        # works we ned to make a query to all the shifts that exist then filter them through the get shifts function
        #give shift a foreign key to shift group
        #shiftgroup gets a shift set for each date
        start_datetime = make_aware(datetime.datetime(2017,5,1), get_default_timezone())
        end_datetime = make_aware(datetime.datetime(2017,5,3), get_default_timezone())
        return Shift.objects.get_shifts_in_datetime_range(start_datetime, end_datetime)




    class Meta:
        app_label = "shifts_app"
        db_table = "shift_group"