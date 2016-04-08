from django.db import models

from shifts_app.shift_group import ShiftGroup

class ShiftManager(models.Manager):
    
    def create(self, start_date, end_date=None):
        pass



class Shift(models.Model):

    #runs_related

    db_table="shift"
    # objects = ShiftManager()

    shift_group = models.ForeignKey(ShiftGroup, related_name="shifts_related")

    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        app_label = "shifts_app"
