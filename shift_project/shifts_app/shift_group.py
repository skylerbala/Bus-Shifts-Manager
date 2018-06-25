from django.db import models
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime

class ShiftGroupManager(models.Manager):
    pass


class ShiftGroup(models.Model):
    #shifts_related = 
    objects = ShiftGroupManager()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    start_date_range = models.DateField()
    end_date_range = models.DateField()

    class Meta:
        app_label = "shifts_app"
        db_table = "shift_groups"

    